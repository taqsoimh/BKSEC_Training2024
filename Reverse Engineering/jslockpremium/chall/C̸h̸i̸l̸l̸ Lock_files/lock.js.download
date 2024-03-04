// Check password here 
const correctPassword = [43490, 822, 2243, 1105, 4652, 429, 1187, 3901, 395, 1067, 622, 457901];

function checkPassword() {
    const dials = document.querySelectorAll('.dial');
    const enteredPassword = Array.from(dials).map(dial => Number(dial.value));
    const decodedPassword = [
        enteredPassword[0] * enteredPassword[1] - 2 * enteredPassword[2],
        enteredPassword[1] + 5 * enteredPassword[2] - 3 * enteredPassword[3],
        enteredPassword[2] + enteredPassword[3] * enteredPassword[4] - enteredPassword[0],
        enteredPassword[5] + 2 * enteredPassword[4] + enteredPassword[2],
        20 * enteredPassword[1] - 2 * enteredPassword[2] - enteredPassword[4],
        enteredPassword[2] + enteredPassword[5] - 2 * enteredPassword[1],
        2 * enteredPassword[1] + enteredPassword[2] + 3 * enteredPassword[6] + 4 * enteredPassword[7],
        5 * enteredPassword[5] - enteredPassword[7] - enteredPassword[8] + 2 * enteredPassword[9],
        3 * enteredPassword[8] + 2 * enteredPassword[9] + 4 * enteredPassword[10] - 3 * enteredPassword[6],
        9 * enteredPassword[11] + 2 * enteredPassword[10] - enteredPassword[8],
        4 * enteredPassword[7] - enteredPassword[8] + enteredPassword[10],
        enteredPassword[3] ** enteredPassword[8] + 3 * enteredPassword[11] - 2 * enteredPassword[7] + enteredPassword[6] + enteredPassword[5] + enteredPassword[10],
    ];
    if (JSON.stringify(decodedPassword) === JSON.stringify(correctPassword)) {
        const passwordString = enteredPassword.join('');
        const hexPassword = new TextEncoder().encode(passwordString).reduce((prev, curr) => prev + curr.toString(16).padStart(2, '0'), '');
        const base64Password = btoa(hexPassword);
        alert("Mở khóa thành công! Cờ của bạn là BKSEC{" + base64Password + "}");
    } else {
        alert('Mật khẩu không chính xác. Vui lòng thử lại.');
    }
}