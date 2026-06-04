document.addEventListener('DOMContentLoaded', () => {
    // Show Loading Overlay on form submit
    const evaluateForm = document.getElementById('evaluateForm');
    if (evaluateForm) {
        evaluateForm.addEventListener('submit', function() {
            document.getElementById('loadingOverlay').classList.add('active');
        });
    }

    // Initialize Chatbot if grades exist
    const gradesDataEl = document.getElementById('grades-data');
    if (!gradesDataEl) return;

    const gradesData = JSON.parse(gradesDataEl.textContent);
    if (!gradesData || gradesData.length === 0) return;

    let conversation = [];
    let currentGradeId = gradesData[0].id;
    let chatOpen = false;

    // Add initial greeting
    conversation.push({
        role: 'assistant',
        content: "Hi there! 👋 I'm GradeBot. What would you like to know about this grade?"
    });

    const chatWindow = document.getElementById('chatWindow');
    const chatFab = document.getElementById('chatFab');
    const chatMessages = document.getElementById('chatMessages');
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendBtn');
    
    // Elements for dynamic updates
    const botGradeInfo = document.getElementById('botGradeInfo');

    window.toggleChat = function() {
        chatOpen = !chatOpen;
        chatWindow.classList.toggle('open', chatOpen);
        chatFab.innerHTML = chatOpen ? '✕' : '🤖';
        if (chatOpen) scrollToBottom();
    };

    function scrollToBottom() {
        if (chatMessages) chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function addMessage(content, role) {
        const div = document.createElement('div');
        div.className = 'chat-msg ' + (role === 'user' ? 'chat-msg-user' : 'chat-msg-bot');
        if (role === 'assistant' || role === 'bot') {
            div.innerHTML = content;
        } else {
            div.textContent = content;
        }
        chatMessages.appendChild(div);
        scrollToBottom();
    }

    function addTyping() {
        const div = document.createElement('div');
        div.className = 'chat-msg chat-msg-bot';
        div.id = 'typingIndicator';
        div.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
        chatMessages.appendChild(div);
        scrollToBottom();
    }

    function removeTyping() {
        const t = document.getElementById('typingIndicator');
        if (t) t.remove();
    }

    window.sendChat = async function() {
        const msg = chatInput.value.trim();
        if (!msg) return;

        chatInput.value = '';
        sendBtn.disabled = true;

        addMessage(msg, 'user');
        conversation.push({ role: 'user', content: msg });
        addTyping();

        try {
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: msg,
                    grade_id: currentGradeId,
                    conversation: conversation
                })
            });
            const data = await res.json();
            removeTyping();
            
            const reply = data.reply || "Sorry, I couldn't process that.";
            addMessage(reply, 'assistant');
            conversation.push({ role: 'assistant', content: reply });
        } catch(e) {
            removeTyping();
            addMessage('Sorry, something went wrong. Try again!', 'assistant');
        }

        sendBtn.disabled = false;
        chatInput.focus();
    };

    window.quickSend = function(msg) {
        if (!chatOpen) toggleChat();
        setTimeout(() => {
            chatInput.value = msg;
            sendChat();
        }, 300);
    };

    window.switchGrade = function(gradeId) {
        currentGradeId = parseInt(gradeId);
        conversation = [];
        chatMessages.innerHTML = '';
        
        // Find new grade to update header
        const newGrade = gradesData.find(g => g.id === currentGradeId);
        if (newGrade) {
            botGradeInfo.textContent = `${newGrade.subject} · ${newGrade.score}/100 · ${newGrade.letter_grade}`;
        }

        addMessage('Switched! Ask me anything about this grade. 😊', 'assistant');
        conversation.push({ role: 'assistant', content: 'Switched grade context!' });
    };
    
    // Handle Enter key
    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') sendChat();
    });
});
