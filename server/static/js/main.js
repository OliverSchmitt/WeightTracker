function getCurrentDateTime() {
    var date = new Date();
    return ("0" + (date.getUTCHours()+2)).slice(-2) + ":" +
        ("0" + date.getUTCMinutes()).slice(-2) + " " +
        ("0" + date.getUTCDate()).slice(-2) + "." +
        ("0" + (date.getUTCMonth()+1)).slice(-2) + " " +
        date.getUTCFullYear();
}
