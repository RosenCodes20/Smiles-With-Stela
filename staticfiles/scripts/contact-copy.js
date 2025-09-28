function copyDiscordUsername() {
    let copyText = 'coding_with_rosen';
    
    let tempInput = document.createElement('input');
    tempInput.value = copyText;
    document.body.appendChild(tempInput);
    
    tempInput.select();
    tempInput.setSelectionRange(0, 99999);
    document.execCommand('copy');
    
    document.body.removeChild(tempInput);
    
    alert('Дискорд името: ' + copyText + ' е копирано!')
    
}

function copyGmail() {
    let gmail = 'sti_857@abv.bg';
    
    let currentInput = document.createElement('input');
    currentInput.value = gmail;
    
    document.body.appendChild(currentInput);
    
    currentInput.select();
    document.execCommand('copy');
    
    currentInput.remove();
    
    alert('Имейлът: ' + gmail + ' е копиран!')
}