//// CCSDSPacket.hpp ////

/*
What is CCSDS Packet Wrapping?
CCSDS = Consultative Committee for Space Data Systems
    - A global standard developed by space agencies (NASA, ESA, JAXA, etc.) to define how data is communicated between spacecraft and ground stations.

CCSDS Packet Wrapping is the process of encapsulating your payload (e.g., telemetry or command data) in a standardized binary packet structure with metadata headers.

CCSDS defines:
    - A primary header (fixed-length, 6 bytes)
    - An optional secondary header (timestamp, origin, etc.)
    - A data field (payload: telemetry or command content)
    - A CRC or checksum (optional)

Why it is imperative and relevant
| Benefit                              | Explanation                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **Real-World Standard**           | NASA, SpaceX, Boeing, etc. all use CCSDS in their telemetry/command formats                                                                           |
|  **Flight Software Authenticity** | CCSDS-compliant packets are the default for space-to-ground and vice versa                                                                            |
|  **Interoperability**              | Using CCSDS ensures compatibility between systems (e.g., between agencies or commercial partners)                                                     |
|  **Encapsulation Layer**           | Abstracts data format from transport (works over TCP, UDP, RF, etc.)                                                                                  |
|  **Validation/Parsing**            | Adds structure that enables automated parsing, routing, and error checking                                                                            |
|  **Great Talking Point**           | can say: “My system simulates command uplink and telemetry downlink over TCP/UDP using CCSDS-compliant packet wrapping for real-world realism.” |


Implementation Plan:
Wrap both command and telemetry payloads using a simple implementation of the CCSDS Primary Header, and insert our plain-text or JSON data as the payload.

| Field                      | Size             | Purpose                                                         |
| -------------------------- | ---------------- | --------------------------------------------------------------- |
| **Version & Type**         | 2 bits + 1 bit   | Packet version (usually `0`) + telemetry (`0`) or command (`1`) |
| **APID**                   | 11 bits          | Application ID (e.g., telemetry = 100, commands = 200)          |
| **Sequence Flags & Count** | 2 bits + 14 bits | Tracks packet order (use 0 or incrementing ID)                  |
| **Packet Length**          | 16 bits          | Payload length – 1 (so a 10-byte payload has length `9`)        |
| **Payload**                | variable         | The actual data (text, binary, JSON, etc.)                      |

Real-world analogy:
A CCSDS packet is to a spacecraft what an envelope is to a letter. You can send anything inside (command, telemetry, even images), 
and the ground system knows how to parse it based on the envelope's header.
*/

#pragma once

#include <cstdint>
#include <vector>
#include <string>
#include <cstring>

struct CCSDSPacket {
    uint16_t versionTypeApid;   // version (3 bits), type (1 bit), APID (11 bits)
    uint16_t sequenceControl;   // sequence flags (2 bits), sequence count (14 bits)
    uint16_t dataLength;        // payload length - 1
    std::vector<uint8_t> payload;

    // create packet from string payload
    static CCSDSPacket create(uint16_t apid, CCSDSPacketType type, uint16_t seqCount, const std::string& payloadStr) {
        CCSDSPacket pkt;

        uint16_t version = 0; // 3 bits
        uint16_t typeBit = static_cast<uint8_t>(type); // 1 bit
        uint16_t apidMasked = apid & 0x07FF; // 11 bits

        pkt.versionTypeApid = (version << 13) | (typeBit << 12) | apidMasked;
        pkt.sequenceControl = (0b11 << 14) | (seqCount & 0x3FFF); // '11' = unsegmented
        pkt.payload = std::vector<uint8_t>(payloadStr.begin(), payloadStr.end());
        pkt.dataLength = pkt.payload.size() > 0 ? pkt.payload.size() - 1 : 0;

        return pkt;
    }

    // serialize packet into a byte array
    std::vector<uint8_t> serialize() const {
        std::vector<uint8_t> buffer(6 + payload.size());

        buffer[0] = versionTypeApid >> 8;
        buffer[1] = versionTypeApid & 0xFF;

        buffer[2] = sequenceControl >> 8;
        buffer[3] = sequenceControl & 0xFF;

        buffer[4] = dataLength >> 8;
        buffer[5] = dataLength & 0xFF;

        std::copy(payload.begin(), payload.end(), buffer.begin() + 6);

        return buffer;
    }

    // deserialize from raw bytes
    static CCSDSPacket deserialize(const std::vector<uint8_t>& raw) {
        if (raw.size() < 6) {
            throw std::runtime_error("Invalid CCSDS packet: too short.");
        }

        CCSDSPacket pkt;
        pkt.versionTypeApid = (raw[0] << 8) | raw[1];
        pkt.sequenceControl = (raw[2] << 8) | raw[3];
        pkt.dataLength = (raw[4] << 8) | raw[5];

        pkt.payload = std::vector<uint8_t>(raw.begin() + 6, raw.end());
        return pkt;
    }

    std::string getPayloadAsString() const {
        return std::string(payload.begin(), payload.end());
    }
};