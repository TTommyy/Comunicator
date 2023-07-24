# Autor: Tomasz Koczar 
# Year : 2023 AD
# File for logging definiton

import inspect
from os import path
from datetime import datetime

def getCurrentTime():
    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_time

def LOG_ENTER():
  time = getCurrentTime()
  former_frame = inspect.currentframe().f_back
  file_name = path.basename(inspect.getsourcefile(former_frame))
  line_number = former_frame.f_lineno
  calling_function_name = former_frame.f_globals["__name__"]
  time = getCurrentTime()
  print(f"{time} [ENTER] File:{file_name}, Fun:{calling_function_name}, Line {line_number}")

def LOG_INFO(info):
  time = getCurrentTime()
  former_frame = inspect.currentframe().f_back
  file_name = path.basename(inspect.getsourcefile(former_frame))
  line_number = former_frame.f_lineno
  calling_function_name = former_frame.f_globals["__name__"]
  time = getCurrentTime()
  print(f"{time}  [INFO] File:{file_name}, Fun:{calling_function_name}, Line {line_number}, Message: {info}")

def LOG_ERROR(error):
  time = getCurrentTime()
  former_frame = inspect.currentframe().f_back
  file_name = path.basename(inspect.getsourcefile(former_frame))
  line_number = former_frame.f_lineno
  calling_function_name = former_frame.f_globals["__name__"]
  print(f"{time} [ERROR] File:{file_name}, Fun:{calling_function_name}, Line {line_number}, Message: {error}")
