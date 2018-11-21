s4day124
内容回顾：
	项目目标：CRM系统/工单/数据库监控系统
	          为学校开发的CRM系统：
					学生
					老师
					销售
					主管
					校长
			  
			  
			  公共组件
			  
			  一套HTML/CSS/JS后台管理模板（No）
			  自定义插件(适用于Python所有Web框架)：
					- 分页
					- Session
					- Form验证
			  公共组件：
					- CURD
					- 权限（基于角色权限管理RBAC）
				
	开发流程：
		1. 需求分析
		
		2. 数据库设计
		
		3. 功能开发：
				分模块：
					登录注册 
					学生管理
						- 提交作业
						- 查看成绩
						- 插件积分
					老师管理
				
				每天早上开会：组长，工程师，项目经理（立项）
				
				一期：
					学员提交个人信息和作业
					销售，客户关系
					
					登录注册 
					学生管理
						- 提交作业
						- 查看成绩
						- 插件积分
					老师管理
				二期：
					老师管理
					班主任管理
					
				三期：
					Bug修改
					页面更加友好
					组件化
				
				
				协同开发：Git/svn
					1. 工作流程
						分支： 
								master线上
								
								release1.0     1.1   1.1
								
								dev    x
								
								PS: 上线周五
									上线：开发负责人、运维人员	
					2.	合并：
							晚上下班前合并
							
					3.	review：
							组长，架构师
							
								master线上
								
								release1.0     1.1   1.1
								
								review            v1
								
								dev    x1   x1    v1
							组长，交给测试部门【功能测试，性能测试】
							
							
				Git重要，给别人的代码贡献： fork
				
				
	具体功能：
		1. 参考Django的admin，开发自定义组件
		   好，臃肿【权限、组合搜索、页面显示，菜单】，开发自己的组件
		   
		   终极目标：
				使用所有Web框架的CURD插件:
					Django[orm]
					tornado[SQLAchemy]
					flask[SQLAchemy]
					bottle[SQLAchemy]
					
					CURD插件+SQLAchemy
					
					
				什么是ORM框架：
					关系对象映射，告别原生SQL，基于类和对象操作数据。
					类   -> 表
					对象 -> 行
					属性 -> 列
				为什么用ORM框架？
					不写SQL语句
				ORM不好？
					性能低
				好？
					快速开发
		   
		2. 启动文件
			AppConfig:
				def ready()
					xxxxx
					
		3. URL
			include本质：[url列表]  appname   namespace
			
			PS: namespace
			
		4. 单例模式
			文件
			
			get_instance()
			
			
			__new__
			
			PS: metaclass
			
		5. site
			registry = {
			
				UserInfo: Base(site,UserInfo)
				Role: Sun(site,UserInfo)
			}
			
			循环进行URL注册
			
		6. 字段
			根据类： 
					获取app名称
					获取表名称
					获取字段：
						字段对象 = UserInfo._meta.get_field('user')
						
						字段对象.model
						字段对象.rel.model
						
		7. 反向生成URL
		
		
		8. request.GET
			- 默认不可修改
			- {k:[1,2,3]}
			
		9. ModelForm
			- 基本用法
			- type创建类
			
		10. 面向对象
			class:
				__init__
					self.namespace
					
					
				xxxxx

			class:
				__iter__
				
				
		11. popup
		
		12 simple_tag,inclusion_tags
		
		13. 功能：
			
			列表页面：
				列表定制列：列名，函数
				Action    ：函数
				  组合搜索：列名，函数
			添加页面：
				ModelForm
			
			编辑页面：
				ModelForm
				
			删除页面：
			
			查看详细：
			
			
			PS： 保留原来URL
				
				
				
今日内容：
	基于组件进行开发
	
	
	1. 基本操作使用
	
	2. 问题:
		/arya/arya/permission/
		/arya/arya/permission/add
		/arya/arya/permission/
		/arya/arya/permission/
		/arya/arya/permission/
		/arya/arya/permission/show
		
		扩展：
			class PermissionAdmin(v1.BaseAryaModal):
				def another_urls(self):
					from django.conf.urls import url
					info = self.model_class._meta.app_label, self.model_class._meta.model_name
					urls = [
						url(r'^show/$', self.show, name='%s_%s_show' % info),
					]
					return urls

				def show(self,request):
					print(request.method)
					current_user_id = request.session['user_info']['nid']

					return render(request,'permission_show.html')

			v1.site.register(models.Permission,PermissionAdmin)

		

	3. CRM
		
		- 组件化
			- CURD
			- 权限
			- 钩子
			
		- 业务流程
			学校：（仓储,电商,4s点）
				招生（销售）
				讲师（搬运工，发货，技工）
				学生（商家）
				主管（主管，经理）
				校长（总监）
				
			需求分析：
				招生老师：8个
					用户表：销售，讲师，
				
					所有客户表（全部）
					
					学员信息： 很多信息
					
					校区
					
					课程：linux，java...
					
					班级
					
		- 增删改查，钩子自定制，页面修改
		
		
		亮点：使用任何程序
			
		
		
					
					
					
					
					
					
					
				
					
					
						
					

				
			
		
		

	
		
		
		
		
		
		
		
		
		
		
		
		
		
						
						
			
			
			
			
			
			
			
			
			
			
					
							
			
							
				
				
				
				
				
				
				
				
				
				
					
			
				
			  
	
	


今日任务：
	1. 项目示例流程检查
	
	2. 权限
	
	3. CRM逻辑
		- 数据库表
		- 操作
		
		
		