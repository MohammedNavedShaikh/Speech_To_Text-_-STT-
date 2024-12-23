let isRecording = false;
let mediaRecorder;
let audioChunks = [];
let audioBlob;
let timerInterval;
let seconds = 0;

function updateTimer() {
    const minutes = Math.floor(seconds / 60);
    const displaySeconds = seconds % 60;
    document.getElementById("timer").textContent = `${String(minutes).padStart(2, '0')}:${String(displaySeconds).padStart(2, '0')}`;
    seconds++;
}

document.getElementById("startBtn").addEventListener("click", async () => {
    if (!isRecording) {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = event => audioChunks.push(event.data);
        mediaRecorder.onstop = () => {
            audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            audioChunks = [];
            const audioFile = new File([audioBlob], 'audio.wav', { type: 'audio/wav' });
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(audioFile);
            document.getElementById('audioFileInput').files = dataTransfer.files;
            document.getElementById("sendBtn").disabled = false;
        };
        mediaRecorder.start();
        isRecording = true;
        document.getElementById("startBtn").disabled = true;
        document.getElementById("stopBtn").disabled = false;
        seconds = 0;
        timerInterval = setInterval(updateTimer, 1000);
    }
});

document.getElementById("stopBtn").addEventListener("click", () => {
    if (mediaRecorder) {
        mediaRecorder.stop();
        isRecording = false;
        document.getElementById("startBtn").innerText = "Start Recording";
        document.getElementById("stopBtn").disabled = true;
        clearInterval(timerInterval);
    }
});

document.getElementById("sendBtn").addEventListener("click", () => {
    document.getElementById("recordingForm").submit();
});
