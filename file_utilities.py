import shutil
import os

def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'text':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'mp3':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'jpge', 'gif', 'raw', 'bmp'):
        return True
    return False

def is_video_file(event):
    if extension_type(event) in ('mp4', 'mov', 'wmv', 'flv', 'avi', 'WebM', 'avchd'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('txt', 'doc', 'docx', 'eps', 'psd', 'cdr', 'ai'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'cs', 'js', 'php', 'html', 'sql', 'css', 'go', 'pas'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False

def make_folder(foldername):
    os.chdir('C:\Users\victo\Downloads')
    if os.path.exists(foldername) == True:
        print('A pasta já existe, pulando a criação')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print('Arquivo movido')
    except:
        print('O arquivo já existia na pasta de destino')
        pass
