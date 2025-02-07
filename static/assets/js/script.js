// <!-- JavaScript for Mobile Menu Toggle -->
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});


function showPopup(message, type) {
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popup-message');

    popupMessage.textContent = message;
    popup.className = `fixed top-5 right-5 px-4 py-3 rounded-lg shadow-md text-white bg-${type}-500`;

    popup.classList.remove('hidden');

    // Hide popup after 5 seconds
    setTimeout(() => {
        popup.classList.add('hidden');
    }, 3000);
}