const readline = require ('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let n1, n2, n3, n4, media;
readline.question('', (n1) => {
    n1 = parseFloat(n1);

    readline.question('', (n2) => {
        n2 = parseFloat(n2);

        readline.question('', (n3) => {
            n3 = parseFloat(n3);

            readline.question('', (n4) => {
                n4 = parseFloat(n4);

                media = (n1+n2+n3+n4)/4;
                console.log(media.toFixed(2));

                readline.close();
            });
        });
    });
});