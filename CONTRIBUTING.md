# 贡献指南

## 开始修改

```bash
git switch main
git pull --ff-only
git switch -c feature/your-change
```

提交前运行：

```bash
python .github/scripts/check_repository.py
```

本检查仅覆盖已跟踪文件。首次添加文件后，可先 `git add <文件>` 再运行检查。业务代码引入后，请同时运行对应的构建和测试。

## Pull Request

先建立范围明确、带验收标准的 Issue，一个 Issue 对应一个 PR。PR 第一行必须为 `Closes #N` 或 `Fixes #N`，只关联本仓库一个开放 Issue；随后按模板说明修改内容及验证结果，正文写作目标为 600 字以内（不含代码块）。提交及 PR 标题使用 `<type>(<scope>): <中文说明>`。

`main` 必须经过 PR；即使是仓库管理员，也受相同保护规则约束。

- 必需检查：`ci-gate`。
- 分支必须与 `main` 保持最新。
- 额外批准人数为 `0`，便于单人维护；PR 流程仍为必需。
- 合并方式：仅 Squash。
- 主线禁止强推和删除，要求线性历史。

GitHub 会自动删除已合并的工作分支。

## 服务器信息

本机 `SERVER_INFO.md` 和密钥文件不纳入版本控制。如需新增部署流程，先明确环境、部署目录和认证方式，再通过 Secrets 配置认证。
