# 仓库配置说明

## 仓库

- 地址：<https://github.com/nhh37740-glitch/ecommerce-agent>
- 可见性：公开。
- 默认分支：`main`。
- 主线保护参考：`nhh37740-glitch/edge-vision-analyzer`。

## 主线保护

| 项目 | 配置 |
| --- | --- |
| 必须通过 Pull Request | 是 |
| 额外批准人数 | 0 |
| 必需状态检查 | `ci-gate`（GitHub Actions） |
| 分支必须保持最新 | 是 |
| 管理员受保护规则约束 | 是 |
| 要求线性历史 | 是 |
| 允许强制推送 | 否 |
| 允许删除主线 | 否 |
| 强制 Code Owner 审核 | 否，与参考仓库一致 |
| 强制提交签名 | 否，与参考仓库一致 |

合并方式仅使用 Squash；关闭 Merge commit 和 Rebase。合并后自动删除工作分支。

## 持续集成

`CI` 工作流在 push、Pull Request 和手动触发时执行，不按路径过滤，避免必需检查因路径过滤而一直等待。

- PR 必须以 `Closes #N` 或 `Fixes #N` 开头，且只关闭本仓库一个开放 Issue；正文写作目标为 600 字以内，沿用参考门禁的 700 字硬性上限（排除已闭合代码块）。
- `repository-checks` 检查基础文件、提交文本格式和意外提交的连接记录、密钥或常见 GitHub 凭据。
- `ci-gate` 始终汇总结果：PR 必须同时通过关联 Issue 检查和仓库检查；push 与手动运行仅跳过 PR 专属规则。失败、取消或异常跳过都不能放行。
- Actions 默认仅有读取权限，禁止工作流创建或批准 PR。
- 第三方 Action 固定到提交 SHA，由 Dependabot 每周检查更新。
- 当前没有业务构建或业务测试，新增应用代码时应增加对应检查。

基础凭据检查仅作补充，不能替代 GitHub secret scanning 或人工检查。

## 协作与安全

- 提供 PR 模板、缺陷和功能 Issue 表单。
- 与参考仓库一致，开启 Issues、Discussions、Wiki 和 Projects。
- 启用 Dependabot 漏洞告警、secret scanning、push protection 和私密漏洞报告。
- Dependabot 自动安全修复保持关闭，与参考仓库一致；启用该功能需另行明确授权。
- Dependabot 版本更新 PR 同样受关联 Issue 规则约束，维护者应先建立对应 Issue，再将 PR 正文首行改为 `Closes #N`，并将正文整理为 600 字以内。
- 未配置部署工作流、部署 Secrets 或 VPS 环境；项目部署目录尚未确定。
- 服务器连接信息仅保存于本地 `SERVER_INFO.md`，不进入版本控制。

## 后续变更

主线保护已启用后，配置文件的修改也应通过工作分支、PR 和 `ci-gate` 完成。远端设置的实际状态可在 GitHub 的 Settings、Actions 和 Security 页面查看。
