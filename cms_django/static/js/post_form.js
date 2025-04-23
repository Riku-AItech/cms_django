document.addEventListener('DOMContentLoaded', function() {
  const waves = document.querySelectorAll('.wave-top, .wave-bottom');
  waves.forEach((wave, index) => {
    let x = 0;
    // 波のスピードを少しずつ変化させる
    const speed = 0.3 + index * 0.1;
    const width = wave.clientWidth;
    function animate() {
      x = (x + speed) % width;
      wave.style.transform = `translateX(${x}px)`;
      requestAnimationFrame(animate);
    }
    animate();
  });
}); 