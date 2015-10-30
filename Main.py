from LoginInterface import LoginGui
from MainInterface import StartScherm

# --- LoginGui deel ---

# Open LoginGui
_LoginGui_lst = LoginGui.Login_Frame.open_interface()
_LoginGui_root = _LoginGui_lst[0]
_LoginGui_class = _LoginGui_lst[1]
_LoginGui_root.mainloop()

# Haal de gebruiker op uit LoginGui
_ingelogde_gebruiker = _LoginGui_class.gebruiker


# --- StartScherm deel ---

# Open StartScherm
_StartScherm_lst = StartScherm.StartScherm.open_interface(_ingelogde_gebruiker)
_StartScherm_root = _StartScherm_lst[0]
_StartScherm_class = _StartScherm_lst[1]
_StartScherm_root.mainloop()
