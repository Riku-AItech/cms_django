// post_list.js
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.post-card');
    cards.forEach((card, index) => {
      card.style.opacity = 0;
      card.style.transform = 'translateY(20px)';
      setTimeout(() => {
        card.style.transition = 'all 0.6s ease';
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
      }, index * 100);

      // 追加: ホバーで浮き出し、クリックで選択ハイライト
      card.addEventListener('mouseenter', () => {
        card.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        card.style.transform = 'translateY(-10px) scale(1.05)';
        card.style.boxShadow = '0 12px 32px rgba(0, 0, 0, 0.15)';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = '';
      });
      card.addEventListener('click', () => {
        if (card.classList.contains('selected')) {
          card.classList.remove('selected');
          card.style.borderColor = '';
        } else {
          card.classList.add('selected');
          card.style.borderColor = '#3B82F6';
        }
      });
    });
  });
  