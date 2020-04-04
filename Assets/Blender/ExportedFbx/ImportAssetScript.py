def ImportAllAssets():
#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#This script will import in unreal all camera in target sequencer
#The script must be used in Unreal Engine Editor with Python plugins : https://docs.unrealengine.com/en-US/Engine/Editor/ScriptingAndAutomation/Python
#Use this command : py "E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\ImportAssetScript.py"


	import os.path
	import ConfigParser
	import ast
	import unreal
	
	
	#Prepare var and def
	unrealImportLocation = r'/Game/ImportedFbx'
	ImportedList = []
	ImportFailList = []
	
	def GetOptionByIniFile(FileLoc, OptionName, literal = False):
		Config = ConfigParser.ConfigParser()
		Config.read(FileLoc)
		Options = []
		if Config.has_section(OptionName):
			for option in Config.options(OptionName):
				if (literal == True):
					Options.append(ast.literal_eval(Config.get(OptionName, option)))
				else:
					Options.append(Config.get(OptionName, option))
		else:
			print("/!\ Option: "+OptionName+" not found in file: "+FileLoc)
		return Options
	
	
	#Process import
	print('========================= Import started ! =========================')
	
	
	
	
	'''
	<##############################################################################>
	<#############################	           		#############################>
	<############################	           		 ############################>
	<############################	 StaticMesh tasks	 ############################>
	<############################	           		 ############################>
	<#############################	           		#############################>
	<##############################################################################>
	'''
	
	StaticMesh_TasksList = []
	StaticMesh_PreImportPath = []
	print('========================= Creating StaticMesh tasks... =========================')
	
	def CreateTask_SM_Wall():
		################[ Import Wall as StaticMesh type ]################
		print('================[ New import task : Wall as StaticMesh type ]================')
		FilePath = os.path.join(r'E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\StaticMesh\SM_Wall.fbx')
		AdditionalParameterLoc = os.path.join(r'E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\StaticMesh\SM_Wall_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : Wall ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "Wall" not found for after inport')
			return
		print('========================= Imports of Wall completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			pass
		print('========================= Post treatment of Wall completed !	 =========================')
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_Wall()
	
	
	
	
	def CreateTask_SM_LeftdoorPanel():
		################[ Import LeftdoorPanel as StaticMesh type ]################
		print('================[ New import task : LeftdoorPanel as StaticMesh type ]================')
		FilePath = os.path.join(r'E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\StaticMesh\SM_LeftdoorPanel.fbx')
		AdditionalParameterLoc = os.path.join(r'E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\StaticMesh\SM_LeftdoorPanel_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : LeftdoorPanel ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "LeftdoorPanel" not found for after inport')
			return
		print('========================= Imports of LeftdoorPanel completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			pass
		print('========================= Post treatment of LeftdoorPanel completed !	 =========================')
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_LeftdoorPanel()
	
	
	
	
	def CreateTask_SM_RightDoorPanel():
		################[ Import RightDoorPanel as StaticMesh type ]################
		print('================[ New import task : RightDoorPanel as StaticMesh type ]================')
		FilePath = os.path.join(r'E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\StaticMesh\SM_RightDoorPanel.fbx')
		AdditionalParameterLoc = os.path.join(r'E:\Videos\Unreal Course\Unreal-YouTube-Course\Assets\Blender\ExportedFbx\StaticMesh\SM_RightDoorPanel_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : RightDoorPanel ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "RightDoorPanel" not found for after inport')
			return
		print('========================= Imports of RightDoorPanel completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			pass
		print('========================= Post treatment of RightDoorPanel completed !	 =========================')
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_RightDoorPanel()
	
	
	
	
	print('========================= Full import completed !  =========================')
	
	StaticMesh_ImportedList = []
	SkeletalMesh_ImportedList = []
	Alembic_ImportedList = []
	Animation_ImportedList = []
	for asset in ImportedList:
		if asset[1] == 'StaticMesh':
			StaticMesh_ImportedList.append(asset[0])
		elif asset[1] == 'SkeletalMesh':
			SkeletalMesh_ImportedList.append(asset[0])
		elif asset[1] == 'Alembic':
			Alembic_ImportedList.append(asset[0])
		else:
			Animation_ImportedList.append(asset[0])
	
	print('Imported StaticMesh: '+str(len(StaticMesh_ImportedList)))
	print('Imported SkeletalMesh: '+str(len(SkeletalMesh_ImportedList)))
	print('Imported Alembic: '+str(len(Alembic_ImportedList)))
	print('Imported Animation: '+str(len(Animation_ImportedList)))
	print('Import failled: '+str(len(ImportFailList)))
	for error in ImportFailList:
		print(error)
	
	#Select asset(s) in content browser
	PathList = []
	for asset in (StaticMesh_ImportedList + SkeletalMesh_ImportedList + Alembic_ImportedList + Animation_ImportedList):
		PathList.append(asset.get_path_name())
	unreal.EditorAssetLibrary.sync_browser_to_objects(PathList)
	
	print('=========================')
	if len(ImportFailList) == 0:
		return 'Assets imported with success !' 
	else:
		return 'Some asset(s) could not be imported.' 
	
print(ImportAllAssets())
