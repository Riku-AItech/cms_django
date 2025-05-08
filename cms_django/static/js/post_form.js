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

  // サムネイル画像の「クリア」チェックボックスのラベルをボタン風に変更
  const imageFieldWrapper = document.querySelector('.image-field-wrapper');
  if (imageFieldWrapper) {
    console.log('Image field wrapper found:', imageFieldWrapper);

    // Django ClearableFileInput の name 属性でクリア用チェックボックスを探す
    const clearCheckbox = imageFieldWrapper.querySelector('input[type="checkbox"][name$="-clear"]');
    let clearLabel = null;

    if (clearCheckbox) {
        console.log('Clear checkbox found:', clearCheckbox);
        // ラベルを探す: 通常は for 属性付き
        clearLabel = imageFieldWrapper.querySelector(`label[for="${clearCheckbox.id}"]`);
        // フォールバック: チェックボックスの次の要素がラベルの可能性
        if (!clearLabel && clearCheckbox.nextElementSibling) {
            clearLabel = clearCheckbox.nextElementSibling;
        }
        if (!clearLabel) {
            console.log('Clear label not found after fallback.');
        }
    } else {
        console.log('Clear checkbox input not found.');
    }

    if (clearLabel && clearCheckbox) {
        console.log('Clear label found:', clearLabel);

        // ラベルのテキストを変更
        clearLabel.textContent = '現在の画像をクリア';

        // ラベルにボタン風スタイルと右寄せクラスを追加
        clearLabel.classList.add(
            'inline-flex', // inline-flexに変更して内部要素を中央揃えしやすくする
            'items-center', // 縦方向中央揃え
            'bg-red-100', 
            'hover:bg-red-200', 
            'text-red-700', 
            'text-xs', 
            'font-semibold', 
            'px-3', 
            'py-1', // パディング調整
            'rounded-full', 
            'cursor-pointer', 
            'ml-4' // 左マージンで右に寄せる (必要なら調整)
        );
        clearLabel.style.verticalAlign = 'middle'; // 他の要素との縦位置を調整

        // ★ チェックボックス自体は非表示にするのをやめる
        // clearCheckbox.style.display = 'none'; // ← この行をコメントアウトまたは削除

        // ★ 代わりに視覚的に隠すスタイルを追加（例）
        clearCheckbox.style.position = 'absolute';
        clearCheckbox.style.opacity = '0';
        clearCheckbox.style.width = '1px'; // 完全に0だとフォーカスできない場合があるため
        clearCheckbox.style.height = '1px';
        clearCheckbox.style.overflow = 'hidden';
        clearCheckbox.style.clip = 'rect(0 0 0 0)'; // 古いブラウザ向け
        clearCheckbox.style.clipPath = 'inset(50%)'; // モダンブラウザ向け

        // ★ 現在のファイル名リンクを探す
        const currentFileLink = imageFieldWrapper.querySelector('a');

        if (currentFileLink) {
            // ★ ラベル（ボタン）をファイル名リンクの直後に移動
            currentFileLink.parentNode.insertBefore(clearLabel, currentFileLink.nextSibling);
            // ★ チェックボックスもラベルの隣に移動させておく（非表示だが）
            clearLabel.parentNode.insertBefore(clearCheckbox, clearLabel.nextSibling);
            // ★ 元々ラベルがあった場所のテキストノード（デフォルトの「クリア」など）を削除する試み
            //    (構造によって調整が必要)
            if (clearCheckbox.nextSibling && clearCheckbox.nextSibling.nodeType === Node.TEXT_NODE ) {
                 clearCheckbox.nextSibling.remove();
            }
            // 例: 「現在:」や「変更:」のテキストノードを削除 (より頑健な方法が必要な場合あり)
            Array.from(imageFieldWrapper.childNodes).forEach(node => {
                if (node.nodeType === Node.TEXT_NODE && (node.textContent.includes('現在:') || node.textContent.includes('変更:'))) {
                    node.textContent = ''; // または node.remove()
                }
            });
            // <br>タグなども不要なら削除
             const brTags = imageFieldWrapper.querySelectorAll('br');
             brTags.forEach(br => br.remove());

        } else {
            console.log('Current file link not found, cannot reposition clear button accurately.');
        }

        // 必要であれば、他のデフォルト表示要素（Currently: や Change: など）を
        // 操作または非表示にするコードもここに追加できます。
    }
  }
}); 