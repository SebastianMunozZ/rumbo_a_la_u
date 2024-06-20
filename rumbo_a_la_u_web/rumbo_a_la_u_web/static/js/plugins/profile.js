document.getElementById('imageUpload').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const profileImage = document.getElementById('profileImage');
            profileImage.src = e.target.result;
            profileImage.style.display = 'block'; // Asegurarse de que la imagen se muestra
        }
        reader.readAsDataURL(file);
    }
});



