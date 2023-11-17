function updateInputClassName() {
    let inputs = document.querySelectorAll("input");
    let textAreas = document.querySelectorAll("textarea");
    let selectDivs = document.querySelectorAll("select");

    [...inputs, ...textAreas, ...selectDivs].forEach(input => {
        if(!input.classList.contains("form-control")) {
            input.classList.add("form-control");
        }
    })
}

updateInputClassName();