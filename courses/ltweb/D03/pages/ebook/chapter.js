import { api } from '../../api.js';

export async function renderEbookChapter(app, { id }) {
  app.innerHTML = `<div class="container page"><div class="loading"><div class="spinner"></div></div></div>`;
  
  const [chapter, allChaptersRes] = await Promise.all([
    api.get(`/ebook/chapters/${id}`),
    api.get('/ebook/chapters').catch(() => ({ chapters: [] }))
  ]);
  const maxChapter = allChaptersRes?.chapters?.length || 5;
  
  app.innerHTML = `
    <div class="container page">
      <div style="margin-bottom:1.5rem">
        <a href="#/ebook" class="btn btn-sm btn-ghost">← Mục lục eBook</a>
      </div>

      <div class="page-header">
        <span class="badge badge-accent">Chương ${chapter.chapter}</span>
        <h1 class="page-title" style="margin-top:0.5rem">${chapter.title}</h1>
        <p class="page-subtitle">Buổi ${chapter.sessions?.join(', ')} · ${chapter.concepts?.length || 0} khái niệm cốt lõi</p>
      </div>

      <!-- SCQA Framework -->
      <div style="margin-bottom:2.5rem">
        <h2 style="margin-bottom:1rem">🧭 Khung SCQA</h2>
        <div class="scqa-flow">
          <div class="scqa-step scqa-s">
            <div class="scqa-step-label">Situation: Bối cảnh</div>
            <p>${chapter.scqa?.situation || ''}</p>
          </div>
          <div class="scqa-step scqa-c">
            <div class="scqa-step-label">Complication: Vấn đề</div>
            <p>${chapter.scqa?.complication || ''}</p>
          </div>
          <div class="scqa-step scqa-q">
            <div class="scqa-step-label">Question: Câu hỏi trung tâm</div>
            <p><strong>${chapter.scqa?.question || ''}</strong></p>
          </div>
          <div class="scqa-step scqa-a">
            <div class="scqa-step-label">Answer: Câu trả lời</div>
            <p>${chapter.scqa?.answer || ''}</p>
          </div>
        </div>
      </div>

      <!-- Core Concepts -->
      <div style="margin-bottom:2.5rem">
        <h2 style="margin-bottom:1rem">💎 Khái niệm cốt lõi</h2>
        <div class="concepts-list" style="display:flex; flex-direction:column; gap:1.25rem">
          ${(chapter.concepts || []).map(c => {
            const listItems = [];
            const blockItems = [];

            (c.key_points || []).forEach(kp => {
              const trimmed = (kp || '').trim();
              if (trimmed.includes('<table') || trimmed.includes('<pre')) {
                blockItems.push(`<div class="concept-table-wrap">${trimmed}</div>`);
              } else {
                listItems.push(`<li style="margin-bottom: 0.4rem; line-height: 1.65;">${trimmed}</li>`);
              }
            });

            return `
            <div class="card concept-card-block" id="concept-${c.id}">
              <div class="card-header" style="padding: 1.25rem 1.5rem 0.5rem; display: flex; flex-direction: column; gap: 0.35rem">
                <span class="badge badge-accent" style="font-size: 0.72rem; align-self: flex-start; text-transform: uppercase; font-weight: 700; letter-spacing: 0.5px">Khái niệm</span>
                <h3 style="margin: 0.2rem 0 0; color: var(--text-primary); font-size: 1.25rem; font-weight: 700">${c.term}</h3>
              </div>
              <div class="card-body" style="padding: 0.75rem 1.5rem 1.5rem">
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 0.85rem 1.15rem; margin-bottom: 1.25rem; font-size: 0.95rem; line-height: 1.65">
                  <strong style="color: var(--accent)">Định nghĩa:</strong> ${c.definition}
                </div>
                ${listItems.length > 0 ? `
                <ul style="font-size: 0.92rem; color: var(--text-secondary); margin: 0 0 1rem; padding-left: 1.3rem">
                  ${listItems.join('')}
                </ul>
                ` : ''}
                ${blockItems.join('')}
                ${c.case_study ? `
                  <div style="margin-top: 1rem; padding: 1rem 1.25rem; background: rgba(59, 130, 246, 0.08); border-radius: var(--radius-sm); border-left: 3px solid var(--info)">
                    <div style="font-size: 0.78rem; font-weight: 700; color: var(--info); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.4rem">📋 Case Study: ${c.case_study.title}</div>
                    <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6">${c.case_study.context}</p>
                    ${c.case_study.lesson_learned ? `
                      <p style="font-size: 0.88rem; color: var(--text-primary); margin-top: 0.5rem; font-weight: 600">
                        → ${c.case_study.lesson_learned}
                      </p>
                    ` : ''}
                  </div>
                ` : ''}
              </div>
            </div>
            `;
          }).join('')}
        </div>
      </div>

      <!-- 3-Level Tests -->
      <div>
        <h2 style="margin-bottom:1rem">🧠 Active Recall: Tự kiểm tra</h2>
        <div class="grid grid-3">
          <a href="#/ebook/chapter/${id}/test/1" class="card" style="text-decoration:none;border-left:3px solid var(--level-1)">
            <div class="level-badge level-1" style="margin-bottom:0.5rem">🎯 Level 1</div>
            <h4>${chapter.tests?.level_1?.name || 'Nắm rõ khái niệm'}</h4>
            <p style="color:var(--text-secondary);font-size:0.85rem;margin-top:0.3rem">
              ${chapter.tests?.level_1?.description || 'Trắc nghiệm: Bạn nhớ đúng không?'}
            </p>
            <p style="font-size:0.75rem;color:var(--text-muted);margin-top:0.5rem">
              Bloom: ${chapter.tests?.level_1?.bloom_level || 'Remember'}
            </p>
          </a>
          <a href="#/ebook/chapter/${id}/test/2" class="card" style="text-decoration:none;border-left:3px solid var(--level-2)">
            <div class="level-badge level-2" style="margin-bottom:0.5rem">📝 Level 2</div>
            <h4>${chapter.tests?.level_2?.name || 'Giải thích'}</h4>
            <p style="color:var(--text-secondary);font-size:0.85rem;margin-top:0.3rem">
              ${chapter.tests?.level_2?.description || 'Tự luận: Giải thích bằng lời bạn'}
            </p>
            <p style="font-size:0.75rem;color:var(--text-muted);margin-top:0.5rem">
              Bloom: ${chapter.tests?.level_2?.bloom_level || 'Understand / Analyze'}
            </p>
          </a>
          <a href="#/ebook/chapter/${id}/test/3" class="card" style="text-decoration:none;border-left:3px solid var(--level-3)">
            <div class="level-badge level-3" style="margin-bottom:0.5rem">🚀 Level 3</div>
            <h4>${chapter.tests?.level_3?.name || 'Vận dụng'}</h4>
            <p style="color:var(--text-secondary);font-size:0.85rem;margin-top:0.3rem">
              ${chapter.tests?.level_3?.description || 'Lên kế hoạch thực tế'}
            </p>
            <p style="font-size:0.75rem;color:var(--text-muted);margin-top:0.5rem">
              Bloom: ${chapter.tests?.level_3?.bloom_level || 'Apply / Create'}
            </p>
          </a>
        </div>
      </div>

      <!-- Navigation -->
      <div style="display:flex;justify-content:space-between;margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--border)">
        ${parseInt(id) > 1 ? `<a href="#/ebook/chapter/${parseInt(id)-1}" class="btn btn-secondary">← Chương ${parseInt(id)-1}</a>` : '<div></div>'}
        ${parseInt(id) < maxChapter ? `<a href="#/ebook/chapter/${parseInt(id)+1}" class="btn btn-primary">Chương ${parseInt(id)+1} →</a>` : '<div></div>'}
      </div>
    </div>
  `;
}
