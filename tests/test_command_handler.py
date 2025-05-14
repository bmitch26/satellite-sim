# # tests/test_command_handler.py

# import queue
# from cubesat.command_handler import CommandHandlerTask

# def test_command_handler_executes_command(capfd):
#     import builtins
#     original_print = builtins.print  # Save original print

#     import rich
#     rich.print = original_print  # Redirect rich.print to plain print during test

#     q = queue.Queue()
#     q.put({"op": "REBOOT", "target": "fault_monitor"})
    
#     task = CommandHandlerTask("CommandHandler")
#     task.run({"tick": 0, "command_queue": q})

#     out, _ = capfd.readouterr()
#     assert "Executing command" in out
#     assert "REBOOT" in out

#     rich.print = rich.__dict__["print"]  # Restore after test

