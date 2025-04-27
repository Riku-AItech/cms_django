// post_list.js
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.post-card');
    cards.forEach((card, index) => {
      // 初期表示アニメーション
      card.style.opacity = 0;
      card.style.transform = 'translateY(20px)';
      setTimeout(() => {
        card.style.transition = 'all 0.6s ease'; // all に戻す
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
      }, index * 100);

      // ホバーエフェクトを元に戻す (少しはっきり浮き上がるバージョン)
      card.addEventListener('mouseenter', () => {
        card.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        card.style.transform = 'translateY(-10px) scale(1.05)';
        card.style.boxShadow = '0 12px 32px rgba(0, 0, 0, 0.15)';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = ''; // 元の影はHTML/CSSで定義される
      });

      // クリック時の選択ハイライト (必要なら残す)
      card.addEventListener('click', (event) => {
         // 編集・削除・投稿者アイコンのクリックはリンク遷移を優先
         if (event.target.closest('a[href*="edit"], button[type="submit"], a[href*="profile_readonly"]')) {
             return; 
         }
         // カード自体のクリックで選択/解除 (ただしリンクでもある)
        if (card.classList.contains('selected')) {
          card.classList.remove('selected');
          // card.style.borderColor = ''; // リング表示と競合するためコメントアウト推奨
        } else {
          // 他の選択済みカードを解除 (任意)
          // document.querySelectorAll('.post-card.selected').forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          // card.style.borderColor = '#3B82F6'; // リング表示と競合するためコメントアウト推奨
        }
      });
    });
  });
  