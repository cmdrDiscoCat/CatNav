; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "CatNav"
#define MyAppVersion "0.0.1"
#define MyAppPublisher "Disco Cat [Les Miyar]"
#define MyAppURL "https://discocat.space/"
#define MyAppExeName "CatNav.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F5AA1879-8CD3-43A0-B3C4-6B2CB5AE05DA}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
OutputBaseFilename=CatNav-setup
SetupIconFile=C:\Users\paind\Desktop\Projets\CatNav\ed.ico
Compression=lzma
SolidCompression=yes

[Languages]


[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\CatNavCatNav.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\tcl\*"; DestDir: "{app}\tcl"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\tk\*"; DestDir: "{app}\tk"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\ed.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\catnav.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\python36.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\paind\Desktop\Projets\CatNav\build\exe.win32-3.6\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\ed.ico"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\ed.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

