document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.post-card');
    cards.forEach((card, index) => {
      // 初期表示アニメーションのみ残す
      card.style.opacity = 0;
      card.style.transform = 'translateY(20px)';
      setTimeout(() => {
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out'; // transform も transition に含める
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
      }, index * 100);

      // ホバー時の影や変形アニメーションは削除
      /*
      card.addEventListener('mouseenter', () => {
        // ... 削除 ...
      });
      card.addEventListener('mouseleave', () => {
        // ... 削除 ...
      });
      card.addEventListener('click', () => {
        // ... 削除 or 必要なら残す ...
      });
      */
    });
  }); 