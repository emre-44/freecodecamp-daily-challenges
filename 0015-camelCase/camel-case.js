function toCamelCase(text) {
    for (const sep of ['-', '_']) {
        text = text.replaceAll(sep, ' ');
    }

    const words = text.split(/\s+/);

    if (!words || words.length === 0 || (words.length === 1 && words[0] === '')) {
        return "";
    }

    let result = words[0].toLowerCase();

    for (let i = 1; i < words.length; i++) {
        const word = words[i];
        if (word && word.length > 0) {
            result += word[0].toUpperCase() + word.slice(1).toLowerCase();
        }
    }

    return result;
}