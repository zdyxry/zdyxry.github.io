document.addEventListener("DOMContentLoaded",function(){const t=document.getElementById("periodTabNav");t&&t.addEventListener("click",function(i){const a=i.target.closest(".period-tab-btn");if(!a)return;const e=a.dataset.period;e&&(document.querySelectorAll(".period-tab-btn").forEach(n=>{n.classList.remove("active")}),a.classList.add("active"),document.querySelectorAll(".period-panel").forEach(n=>{n.classList.remove("active"),n.dataset.panel===e&&n.classList.add("active")}))})});function y(t){const i=t.match(/(\d+)小时/),a=t.match(/(\d+)分钟/),e=i?parseInt(i[1]):0,n=a?parseInt(a[1]):0;return e>0&&n>0?`${e}h${n}m`:e>0?`${e}h`:`${n}m`}const k={0:"未知",1:"Z1 恢复",2:"Z2 有氧",3:"Z3 节奏",4:"Z4 阈值",5:"Z5 最大"},p={0:"var(--text-secondary)",1:"#4ade80",2:"#60a5fa",3:"#fbbf24",4:"#fb923c",5:"#f87171"},f=document.getElementById("loadMoreBtn"),w=document.getElementById("runList");if(f&&w){const t=JSON.parse(w.dataset.allRuns||"[]");let i=!1;f.addEventListener("click",()=>{i?(w.querySelectorAll(".run-card").forEach((e,n)=>{n>=10&&e.remove()}),f.innerHTML=`
          <span>更多</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        `,i=!1,w.scrollIntoView({behavior:"smooth",block:"start"})):(t.slice(10).forEach((e,n)=>{const r=document.createElement("div");r.className="run-card",r.style.animation="fadeIn 0.3s ease",r.dataset.runIndex=10+n,r.dataset.run=JSON.stringify(e);const $=e.hr_zone>0?`
            <span 
              class="hr-zone-badge"
              style="background-color: ${p[e.hr_zone]}20; color: ${p[e.hr_zone]}; border: 1px solid ${p[e.hr_zone]}40;"
            >
              ${k[e.hr_zone]}
            </span>
          `:"",u=`
            <div class="stat vdot-stat">
              <span class="stat-value">${e.vdot??"-"}</span>
              <span class="stat-label">VDOT</span>
            </div>
          `,g=e.training_load>0?`
            <div class="stat load-stat">
              <span class="stat-value">${e.training_load}</span>
              <span class="stat-label">负荷</span>
            </div>
          `:"";r.innerHTML=`
            <div class="run-main">
              <div class="run-header">
                <time class="run-date">${e.date.split(" ")[0]}</time>
                ${$}
              </div>
              <span class="run-type">
                ${e.activity_type||"室外跑步"}
                ${e.workout_name?`<span class="workout-name"> · ${e.workout_name}</span>`:""}
              </span>
            </div>
            <div class="run-stats">
              <div class="stat">
                <span class="stat-value">${e.distance.toFixed(1)}</span>
                <span class="stat-label">km</span>
              </div>
              <div class="stat">
                <span class="stat-value">${y(e.duration)}</span>
                <span class="stat-label">时长</span>
              </div>
              <div class="stat">
                <span class="stat-value">${e.pace}</span>
                <span class="stat-label">配速</span>
              </div>
              ${u}
              ${g}
            </div>
          `,r.addEventListener("click",()=>L(e)),w.appendChild(r)}),f.innerHTML=`
          <span>收起</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(180deg);"><polyline points="6 9 12 15 18 9"></polyline></svg>
        `,i=!0)})}const m=document.getElementById("runDetailModal"),z=document.getElementById("modalBody"),C=document.getElementById("modalClose"),E=m?.querySelector(".modal-overlay");function L(t){if(!m||!z)return;const i=t.hr_zone>0?`
      <span class="detail-hr-zone" style="background-color: ${p[t.hr_zone]}20; color: ${p[t.hr_zone]}; border: 1px solid ${p[t.hr_zone]}40;">
        ${k[t.hr_zone]}
      </span>
    `:"",a={distance:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',duration:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',pace:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>',heartRate:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',cadence:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="1"></circle><path d="M9 20l3-6 3 6"></path><path d="M6 8l6 2 6-2"></path><path d="M12 10V4"></path></svg>',stride:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"></path><path d="M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-6"></path><path d="M12 2v10"></path></svg>',power:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>',calories:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"></path></svg>',elevation:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',vdot:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>',load:'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2z"></path></svg>'},e=[];e.push({icon:a.distance,label:"距离",value:`${t.distance.toFixed(2)} km`}),e.push({icon:a.duration,label:"移动时间",value:y(t.duration)}),e.push({icon:a.duration,label:"总时间",value:y(t.duration)}),e.push({icon:a.pace,label:"配速",value:`${t.pace} /km`}),t.heart_rate>0&&e.push({icon:a.heartRate,label:"平均心率",value:`${Math.round(t.heart_rate)} bpm`}),t.max_heart_rate>0&&e.push({icon:a.heartRate,label:"最大心率",value:`${Math.round(t.max_heart_rate)} bpm`}),t.cadence>0&&e.push({icon:a.cadence,label:"步频",value:`${Math.round(t.cadence)} spm`}),t.stride_length>0&&e.push({icon:a.stride,label:"步幅",value:`${Math.round(t.stride_length)} cm`}),t.avg_power>0&&e.push({icon:a.power,label:"平均功率",value:`${Math.round(t.avg_power)} w`}),t.max_power>0&&e.push({icon:a.power,label:"最大功率",value:`${Math.round(t.max_power)} w`}),t.calories>0&&e.push({icon:a.calories,label:"热量消耗",value:`${Math.round(t.calories)} kcal`}),t.elevation_gain>0&&e.push({icon:a.elevation,label:"累计爬升",value:`${Math.round(t.elevation_gain)} m`}),t.vdot>0&&e.push({icon:a.vdot,label:"VDOT",value:t.vdot.toFixed(1)}),t.training_load>0&&e.push({icon:a.load,label:"训练负荷",value:t.training_load});function n(l){if(!l||l===`0'00"`)return 0;const o=l.match(/(\d+)'(\d+)/);return o?parseInt(o[1])*60+parseInt(o[2]):0}function r(l,o=[]){const s=n(l);if(s===0)return 0;if(o.length>1){const v=o.map(d=>n(d)).filter(d=>d>0);if(v.length>1){const d=Math.min(...v),M=Math.max(...v),_=M-d;if(_>0){const B=(M-s)/_;return Math.max(30,Math.min(100,30+B*70))}}}const c=240,h=480,b=(h-s)/(h-c);return Math.max(20,Math.min(100,20+b*80))}function $(l){const o=n(l);return o===0?"medium":o<330?"fast":o>420?"slow":"medium"}let u="";if(t.segments&&t.segments.length>0){const l=t.segments.map(s=>s.pace).filter(s=>s&&s!==`0'00"`);u=`
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
                ${t.segments.map((s,c)=>{const h=s.hr_zone?`zone-${s.hr_zone}`:"",b=s.hr_zone?k[s.hr_zone]?.split(" ")[0]:"",v=r(s.pace,l),d=$(s.pace);return`
          <tr>
            <td>${s.km||c+1}</td>
            <td>
              <div class="pace-bar">
                <div class="pace-bar-fill ${d}" style="width: ${v}%"></div>
                <span>${s.pace}</span>
              </div>
            </td>
            <td>${s.gap||s.pace}</td>
            <td>
              <span class="hr-zone-tag ${h}">${s.heart_rate||"-"} ${b}</span>
            </td>
          </tr>
        `}).join("")}
              </tbody>
            </table>
          </div>
        </div>
      `}let g="";t.laps&&t.laps.length>0&&(g=`
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
                ${t.laps.map((o,s)=>{const c=o.hr_zone?`zone-${o.hr_zone}`:"",h=o.hr_zone?k[o.hr_zone]?.split(" ")[0]:"";return`
          <tr>
            <td>${s+1}</td>
            <td>${o.distance?.toFixed(2)||"-"}</td>
            <td>
              <span class="pace-tag ${c}">${o.pace||"-"}</span>
            </td>
            <td>${o.cadence||"-"}</td>
            <td>${o.power||"-"}</td>
            <td>
              <span class="hr-zone-tag ${c}">${o.heart_rate||"-"} ${h}</span>
            </td>
          </tr>
        `}).join("")}
              </tbody>
            </table>
          </div>
        </div>
      `),z.innerHTML=`
      <div class="detail-header">
        <h3 class="detail-title">${t.workout_name||"跑步"}</h3>
        <div class="detail-meta">
          <span class="detail-date">${t.date}</span>
          ${i}
          <span class="detail-type">${t.activity_type||"室外跑步"}</span>
        </div>
      </div>
      
      <div class="detail-stats-grid">
        ${e.map(l=>`
          <div class="detail-stat-item">
            <span class="detail-stat-icon">${l.icon}</span>
            <span class="detail-stat-label">${l.label}</span>
            <span class="detail-stat-value">${l.value}</span>
          </div>
        `).join("")}
      </div>
      
      ${u}
      ${g}
    `,m.classList.add("active"),document.body.style.overflow="hidden"}function x(){m&&(m.classList.remove("active"),document.body.style.overflow="")}document.querySelectorAll(".run-card").forEach(t=>{t.addEventListener("click",()=>{const i=t.dataset.run;i&&L(JSON.parse(i))})});C?.addEventListener("click",x);E?.addEventListener("click",x);document.addEventListener("keydown",t=>{t.key==="Escape"&&x()});
