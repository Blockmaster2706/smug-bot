def command_help(command="help"):
    isLanguageGerman = False

    if isLanguageGerman:
        match (command):
            case "help-slash":
                return "Dieser Befehl. Zeigt Hilfe für den angegebenen Befehl.\nSyntax: /help befehl:(BEFEHL)\n\nNutze '/help commands' um eine Liste aller Befehle zu erhalten."
            case "help":
                return "Dieser Befehl. Zeigt Hilfe für den angegebenen Befehl.\nSyntax: %help (BEFEHL)\n\nNutze 'help commands' um eine Liste aller Befehle zu erhalten."
            case "setlogs":
                return 'Setzt den Channel in dem Befehle gelogt werden. Entfernt den LogChannel falls die Aktion "Entfernen" ist. Channel als ID angeben. Admin only.'
            case "database":
                return "Der Befehl um direkt mit der Datenbank zu interagieren. Nur für den Entwickler."
            case "reminder":
                return "Nutze diesen Befehl um den Bot dich an etwas erinnern zu lassen. Syntax: /reminder erinnerung: (NACHRICHT) stunden: x(optional) minuten: x(optional) sekunden: x(optional)"
            case "commandtoggle":
                return "Schaltet Befehle ein oder aus. Nur für den Entwickler."
            case "soe":
                return "Nur ein kleiner Test Befehl"
            case "farbrolle":
                return "Gibt dem Nutzer eine Farbrolle oder bearbeitet sie. Die Farbe kann mit oder ohne # genannt werden und ist als Hex Code einzugeben. Der Standard ist Weiß. \nSyntax: %farbrolle (FARBE)"
            case "commands":

                returnText = "Hier ist eine Liste aller Befehle:\n"
                for command in commands:
                    returnText += "{}\n".format(command)
                return returnText
            
            case _:
                return "Unbekannter Befehl"
    else:
        match (command):
            case "help-slash":
                return "This Command. Shows help for the given command.\nSyntax: /help command:(COMMAND)\n\nUse '/help commands' to get a list of all Commands."
            case "help":
                return "This Command. Shows help for the given command.\nSyntax: %help (COMMAND)\n\nUse 'help commands' to get a list of all Commands."
            case "setlogs":
                return 'Sets the channel in which Commands are logged. Removes the Logchannel if the action is "Remove". Supply the Channel as an ID. Admin only.'
            case "database":
                return "The command to directy interact with the database. Only for the Developer."
            case "reminder":
                return "Use this command to let yourself be reminded of something. Syntax: /reminder reminder: (MESSAGe) hours: x(optional) minutes: x(optional) seconds: x(optional)"
            case "commandtoggle":
                return "Turns commands on or off. Only for the Developer."
            case "test":
                return "Just a little test command."
            case "colorrole":
                return "Gives the user a color role or edits it. The color can be supplied with or without the # and is to be supplied as a Hex Code. The default is white. \nSyntax: %colorrole (color)"
            case "commands":

                returnText = "Here's a list of all commands:\n"
                for command in commands:
                    returnText += "{}\n".format(command)
                return returnText
            
            case _:
                return "Unknown Command."

commands = ( "help-slash", "help", "setlogs", "database", "commandtoggle")