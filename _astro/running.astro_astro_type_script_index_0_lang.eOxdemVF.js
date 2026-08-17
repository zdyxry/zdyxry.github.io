document.addEventListener(`DOMContentLoaded`,function(){let e=document.getElementById(`periodTabNav`);e&&e.addEventListener(`click`,function(e){let t=e.target.closest(`.period-tab-btn`);if(!t)return;let n=t.dataset.period;n&&(document.querySelectorAll(`.period-tab-btn`).forEach(e=>{e.classList.remove(`active`)}),t.classList.add(`active`),document.querySelectorAll(`.period-panel`).forEach(e=>{e.classList.remove(`active`),e.dataset.panel===n&&e.classList.add(`active`)}))})});function e(e){let t=e.match(/(\d+)小时/),n=e.match(/(\d+)分钟/),r=t?parseInt(t[1]):0,i=n?parseInt(n[1]):0;return r>0&&i>0?`${r}h${i}m`:r>0?`${r}h`:`${i}m`}var t={0:`未知`,1:`Z1 恢复`,2:`Z2 有氧`,3:`Z3 节奏`,4:`Z4 阈值`,5:`Z5 最大`},n={0:`var(--text-secondary)`,1:`#4ade80`,2:`#60a5fa`,3:`#fbbf24`,4:`#fb923c`,5:`#f87171`},r=document.getElementById(`loadMoreBtn`),i=document.getElementById(`runList`);if(r&&i){let a=JSON.parse(i.dataset.allRuns||`[]`),o=!1;r.addEventListener(`click`,()=>{o?(i.querySelectorAll(`.run-card`).forEach((e,t)=>{t>=10&&e.remove()}),r.innerHTML=`
          <span>更多</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        `,o=!1,i.scrollIntoView({behavior:`smooth`,block:`start`})):(a.slice(10).forEach((r,a)=>{let o=document.createElement(`div`);o.className=`run-card`,o.style.animation=`fadeIn 0.3s ease`,o.dataset.runIndex=10+a,o.dataset.run=JSON.stringify(r);let s=r.hr_zone>0?`
            <span 
              class="hr-zone-badge"
              style="background-color: ${n[r.hr_zone]}20; color: ${n[r.hr_zone]}; border: 1px solid ${n[r.hr_zone]}40;"
            >
              ${t[r.hr_zone]}
            </span>
          `:``,c=`
            <div class="stat vdot-stat">
              <span class="stat-value">${r.vdot??`-`}</span>
              <span class="stat-label">VDOT</span>
            </div>
          `,u=r.training_load>0?`
            <div class="stat load-stat">
              <span class="stat-value">${r.training_load}</span>
              <span class="stat-label">负荷</span>
            </div>
          `:``;o.innerHTML=`
            <div class="run-main">
              <div class="run-header">
                <time class="run-date">${r.date.split(` `)[0]}</time>
                ${s}
              </div>
              <span class="run-type">
                ${r.activity_type||`室外跑步`}
                ${r.workout_name?`<span class="workout-name"> · ${r.workout_name}</span>`:``}
              </span>
            </div>
            <div class="run-stats">
              <div class="stat">
                <span class="stat-value">${r.distance.toFixed(1)}</span>
                <span class="stat-label">km</span>
              </div>
              <div class="stat">
                <span class="stat-value">${e(r.duration)}</span>
                <span class="stat-label">时长</span>
              </div>
              <div class="stat">
                <span class="stat-value">${r.pace}</span>
                <span class="stat-label">配速</span>
              </div>
              ${c}
              ${u}
            </div>
          `,o.addEventListener(`click`,()=>l(r)),i.appendChild(o)}),r.innerHTML=`
          <span>收起</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(180deg);"><polyline points="6 9 12 15 18 9"></polyline></svg>
        `,o=!0)})}var a=document.getElementById(`runDetailModal`),o=document.getElementById(`modalBody`),s=document.getElementById(`modalClose`),c=a?.querySelector(`.modal-overlay`);function l(r){if(!a||!o)return;let i=r.hr_zone>0?`
      <span class="detail-hr-zone" style="background-color: ${n[r.hr_zone]}20; color: ${n[r.hr_zone]}; border: 1px solid ${n[r.hr_zone]}40;">
        ${t[r.hr_zone]}
      </span>
    `:``,s={distance:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>`,duration:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`,pace:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>`,heartRate:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>`,cadence:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="1"></circle><path d="M9 20l3-6 3 6"></path><path d="M6 8l6 2 6-2"></path><path d="M12 10V4"></path></svg>`,stride:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"></path><path d="M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-6"></path><path d="M12 2v10"></path></svg>`,power:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>`,calories:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"></path></svg>`,elevation:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>`,vdot:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>`,load:`<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2z"></path></svg>`},c=[];c.push({icon:s.distance,label:`距离`,value:`${r.distance.toFixed(2)} km`}),c.push({icon:s.duration,label:`移动时间`,value:e(r.duration)}),c.push({icon:s.duration,label:`总时间`,value:e(r.duration)}),c.push({icon:s.pace,label:`配速`,value:`${r.pace} /km`}),r.heart_rate>0&&c.push({icon:s.heartRate,label:`平均心率`,value:`${Math.round(r.heart_rate)} bpm`}),r.max_heart_rate>0&&c.push({icon:s.heartRate,label:`最大心率`,value:`${Math.round(r.max_heart_rate)} bpm`}),r.cadence>0&&c.push({icon:s.cadence,label:`步频`,value:`${Math.round(r.cadence)} spm`}),r.stride_length>0&&c.push({icon:s.stride,label:`步幅`,value:`${Math.round(r.stride_length)} cm`}),r.avg_power>0&&c.push({icon:s.power,label:`平均功率`,value:`${Math.round(r.avg_power)} w`}),r.max_power>0&&c.push({icon:s.power,label:`最大功率`,value:`${Math.round(r.max_power)} w`}),r.calories>0&&c.push({icon:s.calories,label:`热量消耗`,value:`${Math.round(r.calories)} kcal`}),r.elevation_gain>0&&c.push({icon:s.elevation,label:`累计爬升`,value:`${Math.round(r.elevation_gain)} m`}),r.vdot>0&&c.push({icon:s.vdot,label:`VDOT`,value:r.vdot.toFixed(1)}),r.training_load>0&&c.push({icon:s.load,label:`训练负荷`,value:r.training_load});function l(e){if(!e||e===`0'00"`)return 0;let t=e.match(/(\d+)'(\d+)/);return t?parseInt(t[1])*60+parseInt(t[2]):0}function u(e,t=[]){let n=l(e);if(n===0)return 0;if(t.length>1){let e=t.map(e=>l(e)).filter(e=>e>0);if(e.length>1){let t=Math.min(...e),r=Math.max(...e),i=r-t;if(i>0){let e=(r-n)/i;return Math.max(30,Math.min(100,30+e*70))}}}let r=(480-n)/240;return Math.max(20,Math.min(100,20+r*80))}function d(e){let t=l(e);return t===0?`medium`:t<330?`fast`:t>420?`slow`:`medium`}let f=``;if(r.segments&&r.segments.length>0){let e=r.segments.map(e=>e.pace).filter(e=>e&&e!==`0'00"`);f=`
        <div class="detail-section">
          <h4 class="section-subtitle">分段数据</h4>
          <div class="segments-table-wrapper">
            <table class="segments-table">
              <thead>
                <tr>
                  <th>公里</th>
                  <th>配速</th>
                  <th>GAP</th>
                  <th>心率</th>
                </tr>
              </thead>
              <tbody>
                ${r.segments.map((n,r)=>{let i=n.hr_zone?`zone-${n.hr_zone}`:``,a=n.hr_zone?t[n.hr_zone]?.split(` `)[0]:``,o=u(n.pace,e),s=d(n.pace);return`
          <tr>
            <td>${n.km||r+1}</td>
            <td>
              <div class="pace-bar">
                <div class="pace-bar-fill ${s}" style="width: ${o}%"></div>
                <span>${n.pace}</span>
              </div>
            </td>
            <td>${n.gap||n.pace}</td>
            <td>
              <span class="hr-zone-tag ${i}">${n.heart_rate||`-`} ${a}</span>
            </td>
          </tr>
        `}).join(``)}
              </tbody>
            </table>
          </div>
        </div>
      `}let p=``;r.laps&&r.laps.length>0&&(p=`
        <div class="detail-section">
          <h4 class="section-subtitle">记圈数据</h4>
          <div class="laps-table-wrapper">
            <table class="laps-table">
              <thead>
                <tr>
                  <th>圈</th>
                  <th>距离(km)</th>
                  <th>配速</th>
                  <th>步频</th>
                  <th>功率</th>
                  <th>心率</th>
                </tr>
              </thead>
              <tbody>
                ${r.laps.map((e,n)=>{let r=e.hr_zone?`zone-${e.hr_zone}`:``,i=e.hr_zone?t[e.hr_zone]?.split(` `)[0]:``;return`
          <tr>
            <td>${n+1}</td>
            <td>${e.distance?.toFixed(2)||`-`}</td>
            <td>
              <span class="pace-tag ${r}">${e.pace||`-`}</span>
            </td>
            <td>${e.cadence||`-`}</td>
            <td>${e.power||`-`}</td>
            <td>
              <span class="hr-zone-tag ${r}">${e.heart_rate||`-`} ${i}</span>
            </td>
          </tr>
        `}).join(``)}
              </tbody>
            </table>
          </div>
        </div>
      `),o.innerHTML=`
      <div class="detail-header">
        <h3 class="detail-title">${r.workout_name||`跑步`}</h3>
        <div class="detail-meta">
          <span class="detail-date">${r.date}</span>
          ${i}
          <span class="detail-type">${r.activity_type||`室外跑步`}</span>
        </div>
      </div>
      
      <div class="detail-stats-grid">
        ${c.map(e=>`
          <div class="detail-stat-item">
            <span class="detail-stat-icon">${e.icon}</span>
            <span class="detail-stat-label">${e.label}</span>
            <span class="detail-stat-value">${e.value}</span>
          </div>
        `).join(``)}
      </div>
      
      ${f}
      ${p}
    `,a.classList.add(`active`),document.body.style.overflow=`hidden`}function u(){a&&(a.classList.remove(`active`),document.body.style.overflow=``)}document.querySelectorAll(`.run-card`).forEach(e=>{e.addEventListener(`click`,()=>{let t=e.dataset.run;t&&l(JSON.parse(t))})}),s?.addEventListener(`click`,u),c?.addEventListener(`click`,u),document.addEventListener(`keydown`,e=>{e.key===`Escape`&&u()});