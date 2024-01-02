from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .set_own_voice import set_own_voice

def voice():
    choices = ['Set own voice', 'List of voices to set', 'List of using voices', 'Exit']
    
    isExit = False

    while isExit == False:
        choiceIndex = get_inquirer_choice("Voice settings", choices)

        match choiceIndex:
            case 0:
                set_own_voice()
            case 1:
                list_of_voices_to_set()
            case 2:
                list_of_using_voices()
            case 3:
                isExit = True
