import os


def create_project_dir(directory):
    """
    Create project directory if idt doesn't exist
    :param directory: name of the directory
    :return: None
    """
    if not os.path.exists(directory):
        print('creating new directory' + directory)
        os.makedirs(directory)


def create_data_file(project_name, base_url):
    """
    create queue.txt and crawled.txt files
    :param project_name: project file name
    :param base_url: base url of the website
    :return: None
    """

    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if os.path.isfile(queue):
        write_file(queue, base_url)
    if os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    """
    Accepts file path and data and write data into the file
    :param path: file path
    :param data: data to be written
    :return: None
    """
    with open(path, 'w') as f:
        f.write(data)


def append_to_file(path, data):
    """
    append data to the file
    """
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file(path):
    open(path, 'w').close()


def file_to_set(file_name):
    """
    Copy unique links from file to the queue
    :param file_name: destination file name
    :return: set of unique links
    """
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    """
    copy contents  of set to file
    :param links: set elements
    :param file_name:  filename
    :return: None
    """
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")
