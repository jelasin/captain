from langchain.messages import ToolMessage
from langchain.agents.middleware import AgentMiddleware

class ErrorHandlingMiddleware(AgentMiddleware):
    """自定义中间件处理工具错误"""
    
    async def awrap_tool_call(self, request, handler):
        """异步工具错误处理"""
        try:
            return await handler(request)
        except Exception as e:
            return ToolMessage(
                content=f"工具执行失败: {str(e)}",
                tool_call_id=request.tool_call["id"]
            )
    
    def wrap_tool_call(self, request, handler):
        """同步工具错误处理（可选）"""
        try:
            return handler(request)
        except Exception as e:
            return ToolMessage(
                content=f"工具执行失败: {str(e)}",
                tool_call_id=request.tool_call["id"]
            )
