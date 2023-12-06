let startBtn = document.querySelector(".start-btn");
let finalImg = document.querySelector(".final-img");
const downloadBtn = document.querySelector('.download-btn');

downloadBtn.style.display = "none";

startBtn.addEventListener("click", () => {
    console.log("start");
    let startConfirm = confirm("確定要啟動ㄇ");
    if(startConfirm){
        let img1File = document.getElementById("img1").files[0];
        let img2File = document.getElementById("img2").files[0];

        if (img1File && img2File) {
            const formData = new FormData();
            formData.append('img1', img1File);
            formData.append('img2', img2File);
        
            // 使用fetch方法將資料傳到後端
            fetch('/api/upload', {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    finalImg.src = "merge.png";
                    downloadBtn.style.display = "inline-block";
                })
                .catch(error => console.error('Error:', error));
        } else {
            console.error('未選擇文件');
            alert('Please select both images');
            return;
        }
    }
});

downloadBtn.addEventListener("click", () => {
    fileName = "merge.png"
    fetch(`/api/download`, {
        method: 'POST',
    })
        .then(response => response.blob())
        .then(blob => {
            // 創建一個 URL 對象
            const url = window.URL.createObjectURL(blob);
            // 創建一個 a 元素，將 URL 賦值給其 href 屬性，並觸發點擊
            const a = document.createElement('a');
            a.href = url;
            a.download = fileName;
            a.click();
            // 釋放 URL 對象
            window.URL.revokeObjectURL(url);
        })
        .catch(error => console.error('Error:', error));
})
