# 个人博客

基于 [Astro](https://astro.build) 构建的静态博客网站。

## 技术栈

- **框架**: [Astro](https://astro.build) v5.16.16
- **UI 框架**: React 19
- **内容格式**: MDX
- **样式**: CSS
- **搜索**: Pagefind
- **代码高亮**: Shiki (github-dark 主题)

## 功能特性

- 📝 支持 MDX 格式的博客文章
- 🔍 基于 Pagefind 的全文搜索
- 🏷️ 标签和分类系统
- 👤 作者页面
- 📊 文章系列（Series）
- 🔗 Wiki 链接支持
- 📰 RSS/Atom 订阅
- 🗺️ 站点地图（Sitemap）
- 🔄 文章重定向支持
- 💬 文章引用（Mentions）
- 🏃 跑步数据追踪（支持 VDOT 跑力和训练负荷）

## 项目结构

```text
/
├── public/                 # 静态资源
├── src/
│   ├── components/         # Astro/React 组件
│   ├── content/           # 内容集合
│   │   └── posts/         # 博客文章（373+ 篇）
│   ├── data/              # 数据文件
│   ├── layouts/           # 页面布局
│   ├── pages/             # 路由页面
│   │   ├── index.astro    # 首页
│   │   ├── about.astro    # 关于页面
│   │   ├── friends.astro  # 友链页面
│   │   ├── running.astro  # 跑步记录
│   │   ├── search.astro   # 搜索页面
│   │   ├── posts/         # 文章列表
│   │   ├── tags/          # 标签页面
│   │   ├── categories/    # 分类页面
│   │   ├── authors/       # 作者页面
│   │   ├── series/        # 系列页面
│   │   └── mentions/      # 引用页面
│   ├── styles/            # 样式文件
│   └── utils/             # 工具函数
├── astro.config.mjs       # Astro 配置
├── backlinks.json         # 反向链接数据
└── package.json
```

## 常用命令

| 命令                | 动作                                           |
| :------------------ | :--------------------------------------------- |
| `npm install`       | 安装依赖                                       |
| `npm run dev`       | 启动开发服务器（http://localhost:4321）        |
| `npm run build`     | 构建生产站点到 `./dist/`                       |
| `npm run preview`   | 本地预览构建结果                               |
| `npm run astro ...` | 运行 Astro CLI 命令                            |

## 配置说明

- **站点地址**: `https://zdyxry.github.io`
- **输出模式**: 静态生成（Static）
- **文章集合**: 使用 Astro Content Collections 管理
- **搜索索引**: 构建时自动生成 Pagefind 索引

## 开发注意事项

1. 文章内容存放在 `src/content/posts/` 目录下
2. 使用 Wiki 链接语法 `[[文章标题]]` 创建内部链接
3. 构建时会自动生成搜索索引和站点地图
4. URL 重定向配置在 `url-mapping.json` 中

## 跑步数据

跑步数据通过 Garmin Connect API 自动同步，包含以下功能：

- **VDOT 跑力计算**: 基于 Jack Daniels' Running Formula 计算跑力值
- **训练负荷**: 根据时长和心率区间计算训练负荷
- **心率区间**: 自动识别 Z1-Z5 心率区间

### 配置心率参数

在 GitHub Secrets 中设置以下可选参数：

- `MAX_HR`: 最大心率（默认 190）
- `RESTING_HR`: 静息心率（默认 55）

### 自动同步流程

GitHub Actions 每天自动执行以下步骤：

1. **获取最近 30 天的 Garmin 数据** - 增量更新跑步记录
2. **重新计算所有记录的 VDOT 和训练负荷** - 确保心率参数调整后所有历史数据都更新
3. **构建并部署网站**

### 本地更新跑步数据

```bash
# 为现有数据计算 VDOT 和训练负荷
python3 scripts/calculate_vdot_for_existing.py

# 获取最近 30 天的数据（需要 Garmin 账号）
uv run scripts/get_garmin_data.py --days 30
```

## 感谢

本项目参考了以下优秀项目的设计和实现：

- [pbRun](https://github.com/xuandao/pbRun) - 跑步数据展示灵感
- [Kaze Run](https://kaze.run/dashboard) - 跑步仪表盘界面设计参考

## 许可证

MIT
