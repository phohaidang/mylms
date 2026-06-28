import { api } from '../api.js';

function escapeHTML(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
}

export async function renderQuizResult(app, { sessionId }) {
  app.innerHTML = `<div class="container page"><div class="loading"><div class="spinner"></div></div></div>`;

  try {
    const result = await api.get(`/quizzes/${sessionId}/results`);
    
    if (!result || !result.attempts || result.attempts.length === 0) {
      app.innerHTML = `
        <div class="container page">
          <div class="alert alert-warning">Chưa có kết quả quiz cho buổi ${sessionId}</div>
          <a href="#/quiz/${sessionId}" class="btn btn-primary">Làm Quiz</a>
        </div>
      `;
      return;
    }

    const { attempt_count, reveal_answers, attempts, questions } = result;

    // Tìm lần làm bài tốt nhất
    const bestAttempt = attempts.reduce((best, curr) => curr.score > best.score ? curr : best, attempts[0]);
    const latestAttempt = attempts[attempts.length - 1];

    const percent = Math.round((bestAttempt.correct_count / bestAttempt.total_questions) * 100);
    const emoji = percent >= 80 ? '🎉' : percent >= 60 ? '👍' : percent >= 40 ? '😐' : '💪';
    const message = percent >= 80 ? 'Xuất sắc!' : percent >= 60 ? 'Khá tốt!' : percent >= 40 ? 'Cần ôn thêm' : 'Hãy ôn lại kỹ hơn!';

    // Chuẩn bị HTML danh sách lịch sử nộp bài
    const attemptsHistoryHTML = attempts.map(a => {
      const dt = new Date(a.submitted_at);
      const dateStr = dt.toLocaleDateString('vi-VN', { day: '2-digit', month: '2-digit' });
      const timeStr = dt.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
      const isBest = a.attempt_number === bestAttempt.attempt_number;
      return `
        <div style="display:flex;justify-content:space-between;align-items:center;padding:0.75rem 1rem;background:var(--bg-input);border:1px solid ${isBest ? 'var(--accent)' : 'var(--border)'};border-radius:var(--radius-sm);margin-bottom:0.5rem">
          <div style="display:flex;align-items:center;gap:0.5rem">
            <span class="badge ${isBest ? 'badge-accent' : 'badge-info'}" style="font-size:0.7rem">Lần ${a.attempt_number}</span>
            <span style="font-size:0.88rem;color:var(--text-secondary)">${dateStr} lúc ${timeStr}</span>
          </div>
          <div style="font-weight:700;color:${isBest ? 'var(--accent)' : 'var(--text-primary)'}">
            ${a.score}/10 ${isBest ? '⭐' : ''}
          </div>
        </div>
      `;
    }).join('');

    // Đếm ngược hoặc thông điệp hành động tiếp theo
    let actionPanelHTML = '';
    if (!reveal_answers && attempt_count < 5) {
      actionPanelHTML = `
        <div style="margin:2rem 0;padding:1.25rem;background:var(--warning-light);border:1px solid rgba(245, 158, 11, 0.2);border-radius:var(--radius-md);text-align:left">
          <h4 style="color:var(--warning);margin-bottom:0.5rem;display:flex;align-items:center;gap:0.4rem">📌 Thông báo tự học (Active Recall)</h4>
          <p style="color:var(--text-secondary);font-size:0.88rem;line-height:1.6">
            Bạn đã làm bài <strong>${attempt_count}/5</strong> lần. Bạn có thể làm lại quiz tối đa 5 lần để khắc sâu trí nhớ và đạt điểm tối đa (lấy điểm cao nhất).
            <br><strong>Đặc biệt:</strong> Ở lần thứ 5, toàn bộ đáp án đúng từng câu và lời giải thích sẽ được hiển thị chi tiết.
          </p>
        </div>
        <div style="display:flex;gap:0.75rem;justify-content:center">
          <a href="#/course" class="btn btn-secondary">📚 Về buổi học</a>
          <a href="#/quiz/${sessionId}" class="btn btn-primary">✏️ Làm lại Quiz (Lần ${attempt_count + 1}/5)</a>
        </div>
      `;
    } else {
      actionPanelHTML = `
        <div style="margin:2rem 0;padding:1.25rem;background:var(--success-light);border:1px solid rgba(34, 197, 94, 0.2);border-radius:var(--radius-md);text-align:left">
          <h4 style="color:var(--success);margin-bottom:0.5rem;display:flex;align-items:center;gap:0.4rem">🎉 Đã mở khóa đáp án chi tiết</h4>
          <p style="color:var(--text-secondary);font-size:0.88rem;line-height:1.6">
            Bạn đã hoàn thành đủ tối đa 5 lần làm bài tự học tích cực!
            <br>Hệ thống đã hiển thị toàn bộ đáp án đúng và lời giải thích chi tiết của từng câu hỏi ở bên dưới để bạn ôn tập.
          </p>
        </div>
        <div style="display:flex;gap:0.75rem;justify-content:center;margin-bottom:2rem">
          <a href="#/course" class="btn btn-secondary">📚 Về buổi học</a>
          <a href="#/ebook" class="btn btn-primary">📖 Ôn tập eBook</a>
        </div>
      `;
    }

    // Phần hiển thị đáp án chi tiết (chỉ khi đã làm đủ 5 lần)
    let answersDetailHTML = '';
    if (reveal_answers && questions && questions.length > 0) {
      answersDetailHTML = `
        <div style="margin-top:3rem;padding-top:2rem;border-top:1px solid var(--border)">
          <h2 style="margin-bottom:1.5rem;text-align:left;display:flex;align-items:center;gap:0.5rem">🔍 Đáp Án Chi Tiết & Lời Giải Thích</h2>
          <div style="text-align:left">
            ${questions.map((q, idx) => {
              // Lấy câu trả lời tương ứng trong lần làm bài cuối cùng (lần 5)
              const studentAns = latestAttempt.answers.find(a => a.question_id === q.id);
              const userSelected = studentAns ? studentAns.selected : null;
              
              let isUserCorrect = false;
              if (q.type === 'mc') {
                isUserCorrect = userSelected === q.correct;
              } else if (q.type === 'tf') {
                const normSelected = (userSelected === true || userSelected === 'true' || userSelected === 'A');
                const normCorrect = (q.correct === true || q.correct === 'true' || q.correct === 'A');
                isUserCorrect = normSelected === normCorrect;
              }

              return `
                <div class="card" style="margin-bottom:1.5rem;background:var(--bg-secondary)">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;flex-wrap:wrap;gap:0.5rem">
                    <div style="display:flex;gap:0.5rem">
                      <span class="badge badge-info">Câu ${idx + 1}/${questions.length}</span>
                      <span class="badge">${q.type === 'mc' ? 'Trắc nghiệm' : 'Đúng/Sai'}</span>
                    </div>
                    <span class="badge ${isUserCorrect ? 'badge-success' : 'badge-danger'}">
                      ${isUserCorrect ? '✅ Đúng' : userSelected === null ? '⚠️ Chưa trả lời' : '❌ Sai'}
                    </span>
                  </div>
                  
                  <h4 style="margin-bottom:1.25rem;line-height:1.6;font-size:1rem">${escapeHTML(q.question)}</h4>
                  
                  ${q.type === 'mc' ? `
                    <div style="display:flex;flex-direction:column;gap:0.5rem">
                      ${q.options.map(opt => {
                        const letter = opt.trim().charAt(0);
                        const isCorrectOption = letter === q.correct;
                        const isSelectedOption = letter === userSelected;
                        
                        let optionStyle = '';
                        let badgeHTML = '';
                        
                        if (isCorrectOption) {
                          optionStyle = 'border-color:var(--success);background:var(--success-light);cursor:default;';
                          badgeHTML = '<span class="badge badge-success" style="margin-left:auto;text-transform:none;font-size:0.7rem">Đáp án đúng</span>';
                        } else if (isSelectedOption) {
                          optionStyle = 'border-color:var(--danger);background:var(--danger-light);cursor:default;';
                          badgeHTML = '<span class="badge badge-danger" style="margin-left:auto;text-transform:none;font-size:0.7rem">Lựa chọn của bạn</span>';
                        } else {
                          optionStyle = 'cursor:default;opacity:0.6;';
                        }
                        
                        return `
                          <div class="quiz-option" style="${optionStyle}">
                            <div class="quiz-option-letter" style="${isCorrectOption ? 'background:var(--success);color:white;' : isSelectedOption ? 'background:var(--danger);color:white;' : ''}">
                              ${letter}
                            </div>
                            <div style="font-size:0.92rem;color:var(--text-primary)">${escapeHTML(opt)}</div>
                            ${badgeHTML}
                          </div>
                        `;
                      }).join('')}
                    </div>
                  ` : `
                    <div style="display:flex;gap:0.75rem">
                      <!-- Đúng (True) Option -->
                      ${(() => {
                        const isTrueCorrect = (q.correct === true || q.correct === 'true' || q.correct === 'A');
                        const isTrueSelected = (userSelected === true || userSelected === 'true' || userSelected === 'A');
                        
                        let optionStyle = 'flex:1;justify-content:center;cursor:default;';
                        let badgeHTML = '';
                        
                        if (isTrueCorrect) {
                          optionStyle += 'border-color:var(--success);background:var(--success-light);';
                          badgeHTML = '<br><span class="badge badge-success" style="margin-top:0.25rem;text-transform:none;font-size:0.65rem">Đáp án đúng</span>';
                        } else if (isTrueSelected) {
                          optionStyle += 'border-color:var(--danger);background:var(--danger-light);';
                          badgeHTML = '<br><span class="badge badge-danger" style="margin-top:0.25rem;text-transform:none;font-size:0.65rem">Lựa chọn của bạn</span>';
                        } else {
                          optionStyle += 'opacity:0.6;';
                        }
                        
                        return `
                          <div class="quiz-option" style="${optionStyle}">
                            <div style="text-align:center">
                              <strong>✅ Đúng (True)</strong>
                              ${badgeHTML}
                            </div>
                          </div>
                        `;
                      })()}
                      
                      <!-- Sai (False) Option -->
                      ${(() => {
                        const isFalseCorrect = (q.correct === false || q.correct === 'false' || q.correct === 'B');
                        const isFalseSelected = (userSelected === false || userSelected === 'false' || userSelected === 'B');
                        
                        let optionStyle = 'flex:1;justify-content:center;cursor:default;';
                        let badgeHTML = '';
                        
                        if (isFalseCorrect) {
                          optionStyle += 'border-color:var(--success);background:var(--success-light);';
                          badgeHTML = '<br><span class="badge badge-success" style="margin-top:0.25rem;text-transform:none;font-size:0.65rem">Đáp án đúng</span>';
                        } else if (isFalseSelected) {
                          optionStyle += 'border-color:var(--danger);background:var(--danger-light);';
                          badgeHTML = '<br><span class="badge badge-danger" style="margin-top:0.25rem;text-transform:none;font-size:0.65rem">Lựa chọn của bạn</span>';
                        } else {
                          optionStyle += 'opacity:0.6;';
                        }
                        
                        return `
                          <div class="quiz-option" style="${optionStyle}">
                            <div style="text-align:center">
                              <strong>❌ Sai (False)</strong>
                              ${badgeHTML}
                            </div>
                          </div>
                        `;
                      })()}
                    </div>
                  `}
                  
                  ${q.explanation ? `
                    <div style="margin-top:1.25rem;padding:1rem 1.25rem;background:var(--accent-light);border-left:3px solid var(--accent);border-radius:var(--radius-sm)">
                      <p style="font-size:0.88rem;color:var(--text-primary);line-height:1.6">
                        <strong>💡 Giải thích chi tiết:</strong> ${escapeHTML(q.explanation)}
                      </p>
                    </div>
                  ` : ''}
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;
    }

    app.innerHTML = `
      <div class="container page" style="max-width:720px">
        <div class="card" style="text-align:center;padding:3rem 2rem;margin-bottom:2rem">
          <div style="font-size:4.5rem;margin-bottom:1rem">${emoji}</div>
          <h1 style="margin-bottom:0.5rem;background:linear-gradient(135deg, var(--text-primary), var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">${message}</h1>
          <p style="color:var(--text-secondary);font-size:0.95rem">Kết quả cao nhất trong các lần làm bài</p>

          <div class="stat-value" style="font-size:4rem;margin:1.5rem 0">${bestAttempt.score}/10</div>

          <p style="color:var(--text-secondary);font-size:1.05rem;margin-bottom:1.5rem">
            Đúng <strong>${bestAttempt.correct_count}</strong> / ${bestAttempt.total_questions} câu (${percent}%)
          </p>

          <div style="max-width:480px;margin:2rem auto 0;text-align:left">
            <h4 style="margin-bottom:0.75rem;color:var(--text-primary);border-bottom:1px solid var(--border);padding-bottom:0.5rem">📜 Lịch sử làm bài (${attempt_count}/5 lần)</h4>
            ${attemptsHistoryHTML}
          </div>

          ${actionPanelHTML}
        </div>

        ${answersDetailHTML}
      </div>
    `;

  } catch (err) {
    app.innerHTML = `
      <div class="container page">
        <div class="alert alert-danger">Lỗi tải kết quả quiz: ${err.message}</div>
        <a href="#/course" class="btn btn-secondary">← Quay lại</a>
      </div>
    `;
  }
}
