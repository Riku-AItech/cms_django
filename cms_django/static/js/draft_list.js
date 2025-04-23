document.addEventListener('DOMContentLoaded', function() {
  const items = document.querySelectorAll('.draft-item');
  items.forEach((item, index) => {
    // 初期状態
    item.style.opacity = 0;
    item.style.transform = 'translateY(20px)';
    // ステaggeredアニメーション
    setTimeout(() => {
      item.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
      item.style.opacity = 1;
      item.style.transform = 'translateY(0)';
    }, index * 100);
  });
}); 