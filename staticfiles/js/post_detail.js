document.addEventListener('DOMContentLoaded', () => {
    // アニメーションさせたい要素を取得
    const title = document.querySelector('.detail-title');
    const thumbnail = document.querySelector('.detail-thumbnail');
    const content = document.querySelector('.detail-content');
    const meta = document.querySelector('.detail-meta');
    const actions = document.querySelector('.detail-actions');

    const elementsToAnimate = [title, thumbnail, content, meta, actions].filter(el => el !== null);

    elementsToAnimate.forEach((el, index) => {
        el.style.opacity = 0;
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';

        // 少しずつ遅延させて表示
        setTimeout(() => {
            el.style.opacity = 1;
            el.style.transform = 'translateY(0)';
        }, index * 150); // 遅延時間を調整 (150ms)
    });
}); 