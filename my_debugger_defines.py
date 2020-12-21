from ctypes import *
# Map the Micrisoft types to ctypes for clarity

WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# Constants
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSLOE = 0x00000010
PROCESS_ALL_ACCESS = 0x001F03FF
DBG_CONTINUE = 0x00010002
INFINITE = 0xFFFFFFFF

# Structures for CreateProcessA() function

class STARTUPINFO(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPTSTR),
        ("lpDesktop", LPTSTR),
        ("lpTitle", LPTSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
    ]

class PROCESS_INFOMATION(Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
    ]
class EXCEPTION_DEBUG_INFO(Structure):
    pass
 
class CREATE_THREAD_DEBUG_INFO(Structure):
    pass

class CREATE_PROCESS_DEBUG_INFO(Structure):
    pass

class EXIT_THREAD_DEBUG_INFO(Structure):
    pass

class LOAD_DLL_DEBUG_INFO(Structure):
    pass

class OUTPUT_DEBUG_STRING_INFO(Structure):
    pass

class RIP_INFO(Structure):
    pass

class N12_DEBUG_EVENT4DOLLAR_39E(Union):
    _fields_ = [
        ("Exception", EXCEPTION_DEBUG_INFO),
        ("CreateThread", CREATE_THREAD_DEBUG_INFO),
        ("CreateProcessInfo", CREATE_PROCESS_DEBUG_INFO),
        ("ExitThread", EXIT_THREAD_DEBUG_INFO),
        ("LoadDll", LOAD_DLL_DEBUG_INFO),
        ("UnloadDll", LOAD_DLL_DEBUG_INFO),
        ("DebugString",OUTPUT_DEBUG_STRING_INFO),
        ("RipInfo", RIP_INFO),
    ]

class DEBUG_EVENT(Structure):
    _fields_ = [
        ("dwDebugEventCode", DWORD),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
        ("u", N12_DEBUG_EVENT4DOLLAR_39E),    
    ]