const formIso = document.getElementById('formIsoBr');
const resultIso = document.getElementById('resultIso');

formIso.addEventListener('submit', async (e) => {
  e.preventDefault();
  resultIso.textContent = '';
  resultIso.className = '';

  const date = document.getElementById('isoInput').value.trim();
  try {
    const response = await fetch('/convert/iso-to-br', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ date })
    });
    const data = await response.json();
    if (response.ok) {
      resultIso.textContent = `Resultado: ${data.converted}`;
      resultIso.classList.add('success');
    } else {
      resultIso.textContent = data.error;
      resultIso.classList.add('error');
    }
  } catch {
    resultIso.textContent = 'Erro ao conectar ao servidor.';
    resultIso.classList.add('error');
  }
});


const formBr = document.getElementById('formBrIso');
const resultBr = document.getElementById('resultBr');

formBr.addEventListener('submit', async (e) => {
  e.preventDefault();
  resultBr.textContent = '';
  resultBr.className = '';

  const date = document.getElementById('brInput').value.trim();
  try {
    const response = await fetch('/convert/br-to-iso', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ date })
    });
    const data = await response.json();
    if (response.ok) {
      resultBr.textContent = `Resultado: ${data.converted}`;
      resultBr.classList.add('success');
    } else {
      resultBr.textContent = data.error;
      resultBr.classList.add('error');
    }
  } catch {
    resultBr.textContent = 'Erro ao conectar ao servidor.';
    resultBr.classList.add('error');
  }
});
