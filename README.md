# 电商 Agent

用于电商场景的 Agent 项目。

当前仓库处于初始化阶段，已配置 Git 协作规则、持续集成和主线保护。业务功能与技术选型将在需求确定后补充。

## 开发协作

1. 从最新的 `main` 创建 `feature/<名称>`、`fix/<名称>` 或 `chore/<名称>` 分支。
2. 完成修改并运行适用的检查。
3. 提交 Pull Request，说明修改目的和验证结果。
4. 一个 Issue 对应一个 PR，PR 首行写 `Closes #N` 或 `Fixes #N`。
5. `ci-gate` 检查通过且分支与主线保持最新后，以 Squash 方式合并。

主线规则沿用 [edge-vision-analyzer](https://github.com/nhh37740-glitch/edge-vision-analyzer)：必须经过 PR，管理员同样受保护，禁止强推与删除，保持线性历史。当前不要求额外的批准人数。

## 文档与配置

- [贡献指南](CONTRIBUTING.md)
- [Agent 协作规则](AGENTS.md)
- [安全问题报告](SECURITY.md)
- [仓库配置说明](docs/repository-setup.md)
- [持续集成工作流](.github/workflows/ci.yml)

服务器连接记录保存在本地 `SERVER_INFO.md`，由 Git 忽略。仓库不包含真实服务器凭据。

## 当前检查

`ci-gate` 检查仓库基础文件、文本格式及意外纳入版本控制的连接记录、密钥文件和常见凭据。可在本机运行：

```bash
python .github/scripts/check_repository.py
```

业务代码加入后，应在持续集成中增加对应的构建、测试和静态检查；当前检查不验证业务行为。
