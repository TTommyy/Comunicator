# Autor: Tomasz Koczar 
# Year : 2023 AD
# File for logging definiton
import inspect
import os

def LOG_ENTER():
  former_frame = inspect.currentframe().f_back
  file_name = os.path.basename(inspect.getsourcefile(former_frame))
  line_number = former_frame.f_lineno
  calling_function_name = former_frame.f_globals["__name__"]
  print(f"[ENTER] File:{file_name}, Fun:{calling_function_name}, Line {line_number}")

def LOG_INFO(info):
  former_frame = inspect.currentframe().f_back
  file_name = os.path.basename(inspect.getsourcefile(former_frame))
  line_number = former_frame.f_lineno
  calling_function_name = former_frame.f_globals["__name__"]
  print(f" [INFO] File:{file_name}, Fun:{calling_function_name}, Line {line_number}, Message: {info}")

def LOG_ERROR(error):
  former_frame = inspect.currentframe().f_back
  file_name = os.path.basename(inspect.getsourcefile(former_frame))
  line_number = former_frame.f_lineno
  calling_function_name = former_frame.f_globals["__name__"]
  print(f"[ERROR] File:{file_name}, Fun:{calling_function_name}, Line {line_number}, Message: {error}")
