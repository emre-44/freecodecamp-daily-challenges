function battle(myArmy, opposingArmy) {
    if (myArmy.length > opposingArmy.length) {
        return "Opponent retreated";
    } else if (opposingArmy.length > myArmy.length) {
        return "We retreated";
    }

    let myWins = 0;
    let opponentWins = 0;

    function getStrength(char) {
        if (char >= 'a' && char <= 'z') {
            return char.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
        } else if (char >= 'A' && char <= 'Z') {
            return char.charCodeAt(0) - 'A'.charCodeAt(0) + 27;
        } else if (char >= '0' && char <= '9') {
            return parseInt(char, 10);
        } else {
            return 0;
        }
    }

    for (let i = 0; i < myArmy.length; i++) {
        let myStrength = getStrength(myArmy[i]);
        let opponentStrength = getStrength(opposingArmy[i]);

        if (myStrength > opponentStrength) {
            myWins++;
        } else if (opponentStrength > myStrength) {
            opponentWins++;
        }
    }

    if (myWins > opponentWins) {
        return "We won";
    } else if (opponentWins > myWins) {
        return "We lost";
    } else {
        return "It was a tie";
    }
}