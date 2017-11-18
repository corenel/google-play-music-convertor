function get_list() {
    let music_elements = document.querySelectorAll(
        ".troubleshooter-table-row"
    );
    let music_log = []
    for (music_node of music_elements) {
        let entry = {
            'filename': music_node.children[0].innerText,
            'date': music_node.children[1].innerText,
            'error': music_node.children[2].innerText,
        }
        music_log.push(entry)
    }
    return music_log
}

function save_list(log, filepath) {
    log_str = JSON.stringify(log)
    console_save(log_str, filepath)
}

// From http://www.declancook.com/save-json-file-from-chrome-developer-tools/
function console_save(data, filename) {
    if (!data) {
        console.error('console.save: No data')
        return;
    }

    if (!filename) filename = 'console.json'

    if (typeof data === "object") {
        data = JSON.stringify(data, undefined, 4)
    }

    var blob = new Blob([data], {
            type: 'text/json'
        }),
        e = document.createEvent('MouseEvents'),
        a = document.createElement('a')

    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
}

log = get_list()
save_list(log, 'music_list.json')
