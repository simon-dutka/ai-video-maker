from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

def change_voice():
    choices = ['Set own voice', 'List of voices', 'Exit']
    isExit = False

    while isExit == False:
        choiceIndex = get_inquirer_choice("Set voice to use", choices)

        match choiceIndex:
            case 0:
                set_own_voice()
            case 1:
                list_of_voices()
            case 2:
                isExit = True
