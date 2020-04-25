Search.setIndex({docnames:["api/finstmt","api/finstmt.bs","api/finstmt.clean","api/finstmt.combined","api/finstmt.config_manage","api/finstmt.findata","api/finstmt.forecast","api/finstmt.forecast.models","api/finstmt.inc","api/finstmt.items","api/finstmt.loaders","api/modules","auto_examples/forecasting","auto_examples/index","auto_examples/sg_execution_times","index","tutorial"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":2,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["api/finstmt.rst","api/finstmt.bs.rst","api/finstmt.clean.rst","api/finstmt.combined.rst","api/finstmt.config_manage.rst","api/finstmt.findata.rst","api/finstmt.forecast.rst","api/finstmt.forecast.models.rst","api/finstmt.inc.rst","api/finstmt.items.rst","api/finstmt.loaders.rst","api/modules.rst","auto_examples/forecasting.rst","auto_examples/index.rst","auto_examples/sg_execution_times.rst","index.rst","tutorial.rst"],objects:{"":{finstmt:[0,0,0,"-"]},"finstmt.bs":{config:[1,0,0,"-"],data:[1,0,0,"-"],main:[1,0,0,"-"]},"finstmt.bs.data":{BalanceSheetData:[1,1,1,""]},"finstmt.bs.data.BalanceSheetData":{__init__:[1,2,1,""],cash:[1,3,1,""],cash_and_st_invest:[1,3,1,""],common_stock:[1,3,1,""],current_lt_debt:[1,3,1,""],def_tax_lt:[1,3,1,""],def_tax_st:[1,3,1,""],deferred_rev:[1,3,1,""],dep:[1,3,1,""],deposit_liab:[1,3,1,""],goodwill:[1,3,1,""],gross_ppe:[1,3,1,""],inventory:[1,3,1,""],items_config:[1,3,1,""],lt_debt:[1,3,1,""],lt_invest:[1,3,1,""],minority_interest:[1,3,1,""],net_ppe:[1,3,1,""],nwc:[1,2,1,""],other_current_assets:[1,3,1,""],other_current_liab:[1,3,1,""],other_income:[1,3,1,""],other_lt_assets:[1,3,1,""],other_lt_liab:[1,3,1,""],payables:[1,3,1,""],receivables:[1,3,1,""],retained_earnings:[1,3,1,""],st_debt:[1,3,1,""],st_invest:[1,3,1,""],tax_liab_lt:[1,3,1,""],tax_liab_st:[1,3,1,""],total_assets:[1,3,1,""],total_current_assets:[1,3,1,""],total_current_liab:[1,3,1,""],total_debt:[1,3,1,""],total_equity:[1,3,1,""],total_liab:[1,3,1,""],total_liab_and_equity:[1,3,1,""],total_non_current_assets:[1,3,1,""],total_non_current_liab:[1,3,1,""]},"finstmt.bs.main":{BalanceSheets:[1,1,1,""]},"finstmt.bs.main.BalanceSheets":{__init__:[1,2,1,""],statement_cls:[1,3,1,""],statement_name:[1,3,1,""],statements:[1,3,1,""]},"finstmt.clean":{name:[2,0,0,"-"]},"finstmt.clean.name":{standardize_name_for_look_up:[2,4,1,""],standardize_names_in_series_index:[2,4,1,""]},"finstmt.combined":{statements:[3,0,0,"-"]},"finstmt.combined.statements":{FinancialStatements:[3,1,1,""]},"finstmt.combined.statements.FinancialStatements":{__init__:[3,2,1,""],balance_sheets:[3,3,1,""],capex:[3,2,1,""],change:[3,2,1,""],fcf:[3,2,1,""],forecast:[3,2,1,""],forecast_assumptions:[3,2,1,""],income_statements:[3,3,1,""],lag:[3,2,1,""],non_cash_expenses:[3,2,1,""]},"finstmt.combined.statements.FinancialStatements.change.params":{data_key:[3,5,1,""]},"finstmt.combined.statements.FinancialStatements.lag.params":{data_key:[3,5,1,""],num_lags:[3,5,1,""]},"finstmt.config_manage":{base:[4,0,0,"-"],data:[4,0,0,"-"],global_:[4,0,0,"-"],statement:[4,0,0,"-"],statements:[4,0,0,"-"]},"finstmt.config_manage.base":{ConfigManagerBase:[4,1,1,""]},"finstmt.config_manage.base.ConfigManagerBase":{eq_subs_dict:[4,2,1,""],expr_for:[4,2,1,""],get:[4,2,1,""],get_value:[4,2,1,""],set:[4,2,1,""],set_value:[4,2,1,""],sympy_namespace:[4,2,1,""]},"finstmt.config_manage.data":{DataConfigManager:[4,1,1,""]},"finstmt.config_manage.data.DataConfigManager":{__init__:[4,2,1,""],config_dict:[4,2,1,""],configs:[4,3,1,""],get:[4,2,1,""],keys:[4,2,1,""],set:[4,2,1,""],sympy_namespace:[4,2,1,""]},"finstmt.config_manage.statement":{StatementConfigManager:[4,1,1,""]},"finstmt.config_manage.statement.StatementConfigManager":{__init__:[4,2,1,""],config_managers:[4,3,1,""],get:[4,2,1,""],items:[4,2,1,""],keys:[4,2,1,""],set:[4,2,1,""],sympy_namespace:[4,2,1,""]},"finstmt.config_manage.statements":{StatementsConfigManager:[4,1,1,""]},"finstmt.config_manage.statements.StatementsConfigManager":{__init__:[4,2,1,""],config_managers:[4,3,1,""],get:[4,2,1,""],keys:[4,2,1,""],set:[4,2,1,""],sympy_namespace:[4,2,1,""],update:[4,2,1,""],update_all:[4,2,1,""]},"finstmt.config_manage.statements.StatementsConfigManager.update.params":{config_keys:[4,5,1,""],item_key:[4,5,1,""],value:[4,5,1,""]},"finstmt.config_manage.statements.StatementsConfigManager.update_all.params":{config_keys:[4,5,1,""],value:[4,5,1,""]},"finstmt.exc":{CouldNotParseException:[0,6,1,""],ForecastException:[0,6,1,""],ForecastNotFitException:[0,6,1,""],ForecastNotPredictedException:[0,6,1,""],ImproperManualForecastException:[0,6,1,""],NoSuchItemException:[0,6,1,""],NotACalculatedItemException:[0,6,1,""]},"finstmt.findata":{database:[5,0,0,"-"],statementsbase:[5,0,0,"-"]},"finstmt.findata.database":{FinDataBase:[5,1,1,""]},"finstmt.findata.database.FinDataBase":{__init__:[5,2,1,""],as_dict:[5,2,1,""],from_series:[5,2,1,""],get_sympy_subs_dict:[5,2,1,""],items_config:[5,3,1,""],prior_statement:[5,3,1,""],to_series:[5,2,1,""]},"finstmt.findata.statementsbase":{FinStatementsBase:[5,1,1,""],combine_statement_dfs:[5,4,1,""]},"finstmt.findata.statementsbase.FinStatementsBase":{__init__:[5,2,1,""],freq:[5,2,1,""],from_df:[5,2,1,""],statement_cls:[5,3,1,""],statement_name:[5,3,1,""],statements:[5,3,1,""],to_df:[5,2,1,""]},"finstmt.forecast":{config:[6,0,0,"-"],dataframe:[6,0,0,"-"],main:[6,0,0,"-"],models:[7,0,0,"-"],plot:[6,0,0,"-"],statements:[6,0,0,"-"]},"finstmt.forecast.config":{ForecastConfig:[6,1,1,""],ForecastItemConfig:[6,1,1,""]},"finstmt.forecast.config.ForecastConfig":{__init__:[6,2,1,""],freq:[6,3,1,""],make_future_df_kwargs:[6,2,1,""],periods:[6,3,1,""],prophet_kwargs:[6,3,1,""]},"finstmt.forecast.config.ForecastItemConfig":{__init__:[6,2,1,""],cap:[6,3,1,""],floor:[6,3,1,""],make_forecast:[6,3,1,""],manual_forecasts:[6,3,1,""],method:[6,3,1,""],pct_of:[6,3,1,""],prophet_kwargs:[6,3,1,""],to_series:[6,2,1,""]},"finstmt.forecast.dataframe":{add_cap_and_floor_to_df:[6,4,1,""]},"finstmt.forecast.main":{Forecast:[6,1,1,""]},"finstmt.forecast.main.Forecast":{__init__:[6,2,1,""],fit:[6,2,1,""],model:[6,3,1,""],name:[6,2,1,""],plot:[6,2,1,""],predict:[6,2,1,""],result:[6,2,1,""],series:[6,2,1,""],to_manual:[6,2,1,""]},"finstmt.forecast.models":{average:[7,0,0,"-"],base:[7,0,0,"-"],cagr:[7,0,0,"-"],chooser:[7,0,0,"-"],manual:[7,0,0,"-"],prophet:[7,0,0,"-"],recent:[7,0,0,"-"],trend:[7,0,0,"-"]},"finstmt.forecast.models.average":{AverageModel:[7,1,1,""]},"finstmt.forecast.models.average.AverageModel":{fit:[7,2,1,""],mean:[7,3,1,""],predict:[7,2,1,""],stderr:[7,3,1,""]},"finstmt.forecast.models.base":{ForecastModel:[7,1,1,""],compare_freq_strs:[7,4,1,""]},"finstmt.forecast.models.base.ForecastModel":{__init__:[7,2,1,""],desired_freq_t_multiplier:[7,2,1,""],fit:[7,2,1,""],historical_freq:[7,2,1,""],last_historical_period:[7,3,1,""],orig_series:[7,3,1,""],plot:[7,2,1,""],predict:[7,2,1,""],result:[7,3,1,""],result_df:[7,3,1,""]},"finstmt.forecast.models.cagr":{CAGRModel:[7,1,1,""]},"finstmt.forecast.models.cagr.CAGRModel":{cagr:[7,3,1,""],fit:[7,2,1,""],last_value:[7,3,1,""],predict:[7,2,1,""],stderr:[7,3,1,""]},"finstmt.forecast.models.chooser":{get_model:[7,4,1,""]},"finstmt.forecast.models.manual":{ManualForecastModel:[7,1,1,""]},"finstmt.forecast.models.manual.ManualForecastModel":{__init__:[7,2,1,""],fit:[7,2,1,""],predict:[7,2,1,""],recent:[7,3,1,""]},"finstmt.forecast.models.prophet":{FBProphetModel:[7,1,1,""]},"finstmt.forecast.models.prophet.FBProphetModel":{__init__:[7,2,1,""],fit:[7,2,1,""],plot:[7,2,1,""],predict:[7,2,1,""]},"finstmt.forecast.models.recent":{RecentValueModel:[7,1,1,""]},"finstmt.forecast.models.recent.RecentValueModel":{fit:[7,2,1,""],predict:[7,2,1,""],recent:[7,3,1,""]},"finstmt.forecast.models.trend":{LinearTrendModel:[7,1,1,""]},"finstmt.forecast.models.trend.LinearTrendModel":{fit:[7,2,1,""],model:[7,3,1,""],model_result:[7,3,1,""],predict:[7,2,1,""]},"finstmt.forecast.plot":{plot_forecast:[6,4,1,""]},"finstmt.forecast.statements":{ForecastedFinancialStatements:[6,1,1,""]},"finstmt.forecast.statements.ForecastedFinancialStatements":{__init__:[6,2,1,""],forecasts:[6,3,1,""],plot:[6,2,1,""]},"finstmt.inc":{config:[8,0,0,"-"],data:[8,0,0,"-"],main:[8,0,0,"-"]},"finstmt.inc.data":{IncomeStatementData:[8,1,1,""]},"finstmt.inc.data.IncomeStatementData":{__init__:[8,2,1,""],cogs:[8,3,1,""],dep_exp:[8,3,1,""],ebit:[8,3,1,""],ebt:[8,3,1,""],effective_tax_rate:[8,2,1,""],gain_on_sale_asset:[8,3,1,""],gain_on_sale_invest:[8,3,1,""],gross_profit:[8,2,1,""],impairment:[8,3,1,""],int_exp:[8,3,1,""],items_config:[8,3,1,""],net_income:[8,3,1,""],op_exp:[8,3,1,""],other_op_exp:[8,3,1,""],rd_exp:[8,3,1,""],revenue:[8,3,1,""],sga:[8,3,1,""],tax_exp:[8,3,1,""]},"finstmt.inc.main":{IncomeStatements:[8,1,1,""]},"finstmt.inc.main.IncomeStatements":{__init__:[8,2,1,""],statement_cls:[8,3,1,""],statement_name:[8,3,1,""],statements:[8,3,1,""]},"finstmt.items":{config:[9,0,0,"-"]},"finstmt.items.config":{ItemConfig:[9,1,1,""]},"finstmt.items.config.ItemConfig":{__init__:[9,2,1,""],display_name:[9,3,1,""],expr_str:[9,3,1,""],extract_names:[9,3,1,""],force_positive:[9,3,1,""],forecast_config:[9,3,1,""],key:[9,3,1,""],primary_name:[9,2,1,""]},"finstmt.loaders":{capiq:[10,0,0,"-"]},"finstmt.loaders.capiq":{load_capiq_df:[10,4,1,""]},finstmt:{bs:[1,0,0,"-"],clean:[2,0,0,"-"],combined:[3,0,0,"-"],config_manage:[4,0,0,"-"],exc:[0,0,0,"-"],findata:[5,0,0,"-"],forecast:[6,0,0,"-"],inc:[8,0,0,"-"],items:[9,0,0,"-"],loaders:[10,0,0,"-"],logger:[0,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","function","Python function"],"5":["py","parameter","Python parameter"],"6":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:function","5":"py:parameter","6":"py:exception"},terms:{"00it":12,"1500x300":12,"1500x4800":12,"15it":12,"20it":12,"22it":12,"38it":12,"41it":12,"49it":12,"55it":12,"56it":12,"67it":12,"69it":12,"82it":12,"88it":12,"8e10":12,"91it":12,"class":[1,2,3,4,5,6,7,8,9,12],"float":[1,4,5,6,7,8],"function":5,"import":12,"int":[1,3,6,8],"long":[1,12],"new":12,"return":[1,2,3,4,5,6,7,8,9,10],"short":[1,12],"true":[1,6,8,9,12],"while":12,And:12,Axes:12,For:[4,12],OLS:7,The:[4,6,7,12,16],Then:12,Used:[2,4],Uses:16,__init__:[1,3,4,5,6,7,8,9],acc:1,access:3,account:1,accum:1,accumul:[1,12],accur:[5,6,7],actual:12,add:5,add_cap_and_floor_to_df:6,added:12,adjust:6,admin:8,administr:8,after:12,again:12,alia:[1,5,8],all:[3,4,12,13],alreadi:12,also:12,amort:[8,12],amp:12,ani:[4,12],annual:[7,16],annual_b:12,annual_incom:12,api:[7,15],appropri:12,arg:5,as_dict:5,asset:[1,8,12],auto:[6,16],auto_exampl:14,auto_examples_jupyt:13,auto_examples_python:13,avail:16,averag:[0,6,16],averagemodel:7,balanc:[1,3,4,12,16],balance_sheet:[3,6],balancesheet:[1,3,6,10,12,16],balancesheetdata:1,base:[0,1,3,5,6,8,9,11],base_config:[6,7],becaus:12,been:12,befor:[2,8,12],begin:12,belong:4,below:13,between:3,binder:12,bool:[6,9],boost:12,borrow:1,borrowst:1,browser:12,bs_data:[1,3,16],bs_df:[1,3,12,16],bs_path:[1,3,12,16],built:5,cagr:[0,1,6,8,12,16],cagrmodel:7,calcul:[0,16],can:[0,10,12],cap:[1,6,8,12],capex:3,capiq:[0,11],capit:10,cash:[0,1,12],cash_and_st_invest:1,cat:12,chang:3,charg:8,chdir:12,chooser:[0,6],chosen:12,classmethod:5,clean:[0,11],click:12,code:[12,13,15],cog:[8,12],column:5,combin:[0,6,11],combine_statement_df:5,come:12,common:[1,12],common_stock:1,comp:1,compare_freq_str:7,compound:16,comprehens:[1,12],config:[0,2,4,7,11,12],config_dict:4,config_kei:4,config_manag:[0,1,8,11],configmanagerbas:4,configur:[4,6,12],construct:[1,8,16],contain:[4,12],conveni:12,cor:8,cost:[8,12],couldnotparseexcept:0,csv:12,curr:1,current:[1,6,12],current_lt_debt:1,currnoncurr:1,data:[0,2,3,5,11,12],data_kei:3,databas:[0,1,8,11,12],dataconfigmanag:[1,4,5,8],datafram:[0,2,3,5,7,10,11],date:[4,5],datetim:7,debt:[1,12],deepcopi:12,def:1,def_tax_lt:1,def_tax_st:1,defer:[1,12],deferred_rev:1,deficit:1,definit:4,dep:[1,8],dep_exp:8,deposit:[1,12],deposit_liab:1,depreci:[1,8,12],desir:12,desired_freq_t_multipli:7,develop:8,df2:5,dict:[1,4,5,6,8],dictionari:12,did:12,directli:5,display_nam:[1,8,9],doesn:12,down:8,download:[10,12,13],each:[4,12,16],earlier:12,earn:[1,8,12],ebit:[8,12],ebt:[8,12],effect:12,effective_tax_r:8,either:12,encount:12,entir:4,eq_subs_dict:4,equip:[1,12],equiti:[1,12],equiv:1,equival:[1,12],everyth:12,exampl:[1,3,8,12,15,16],exc:[11,15],except:0,execut:14,exp:8,expens:[8,12],expenseinc:8,expenseincom:8,expensesinc:8,expensesincom:8,experi:12,expinc:8,expincom:8,expr:4,expr_for:4,expr_str:[1,8,9],extract:12,extract_nam:[1,8,9],factori:[6,9],fals:[1,6,8],fbprophet:[6,16],fbprophetmodel:7,fcf:3,fcst:12,fcst_df:6,few:12,figsiz:[6,7],figur:[6,7,12],file:14,file_path:10,financi:[0,3,4,5,6,10,13,14,16],financialstat:[3,6,12,16],find:15,findata:[0,1,8,11,12],findatabas:[1,5,8],finstatementsbas:[1,5,8],finstmt:[13,14],fit:[6,7,16],floor:[1,6,8,12],floot:6,flow:0,focu:12,force_posit:[1,8,9],forecast:[0,3,9,11,13,14,15],forecast_assumpt:[3,12],forecast_config:[1,8,9,12],forecastconfig:6,forecastedfinancialstat:[6,12],forecastexcept:0,forecastitemconfig:[1,6,8,9],forecastmodel:[6,7],forecastnotfitexcept:0,forecastnotpredictedexcept:0,format:12,forwardref:[1,8],free:0,freq1:7,freq2:7,freq:[5,6],frequenc:7,frequnci:7,from:[10,12],from_df:[1,3,5,8,12,16],from_seri:5,full:12,futur:16,gain:[8,12],gain_on_sale_asset:8,gain_on_sale_invest:8,galleri:[12,13],gener:[8,12,13],get:[3,4,12,15],get_model:7,get_sympy_subs_dict:5,get_valu:4,github:15,global_:[0,11],going:12,good:[8,12],goodwil:[1,8,12],gross:[1,8,12],gross_pp:1,gross_profit:8,grosss:[1,12],grow:16,growth:[1,8,12,16],grs:1,had:12,handl:4,has:12,have:[5,12],help:[0,5,6,7],here:[12,15],histor:[7,16],historical_freq:7,hold:[1,3,8],home:12,how:3,impair:[8,12],impropermanualforecastexcept:0,inc:[0,1,3,6,11,12],inc_data:[3,8,16],inc_df:[3,8,12,16],inc_path:[3,8,12,16],incl:8,includ:8,incom:[1,3,4,8,12,16],income_stat:[3,6],incomestat:[3,6,8,10,12,16],incomestatementdata:8,index:[5,12,15],index_col:12,indexedbas:[4,5],individu:[4,6],initi:[5,6,7],inplac:2,instal:15,int_exp:8,intang:[1,12],interest:[1,8,12],interfac:4,intern:[2,4],inv:1,invalid:12,inventori:[1,12],invest:[1,8,12],ipynb:12,item:[0,1,4,5,6,8,11,12],item_config:[6,7,12],item_kei:4,itemconfig:[1,4,5,8,9],items_config:[1,5,8],join:12,jupyt:[12,13],just:12,kei:[1,3,4,6,8,9,12],kwarg:[3,5,6],lag:3,last:3,last_historical_period:7,last_valu:[7,12],let:12,level:[1,8,12],liab:1,liabil:[1,12],line:6,linear:16,linear_model:7,lineartrendmodel:7,list:[1,4,5,6,8,12],load:10,load_capiq_df:10,loader:[0,11],logger:[11,15],longterm:1,look:[2,15],loss:8,lt_debt:1,lt_invest:1,main:[0,3,4,11],make:12,make_forecast:[1,6,8],make_future_df_kwarg:6,manag:4,manual:[0,6,12],manual_forecast:[1,6,8],manualforecastmodel:7,match:2,maximum:6,mean:[7,12,16],messag:12,method:[1,6,8,16],min:1,minimum:6,minor:[1,12],minority_interest:1,minut:12,model:[0,6,12],model_result:7,modul:[11,15],more:12,most:16,multipl:[4,12],multipli:7,must:5,name:[0,5,6,11],namespac:4,necessari:12,need:[4,12],nest:4,net:[1,8,12],net_incom:8,net_pp:1,netcommon:1,next_valu:12,non:[1,12],non_cash_expens:3,noncurr:1,none:[1,3,4,5,6,7,8,9,12],nonetyp:[1,8,9],nosuchitemexcept:0,notacalculateditemexcept:0,note:[2,12],notebook:[12,13,16],now:12,num_lag:3,number:3,nwc:1,object:[3,4,5,6,7,9,12],oca:1,off:12,often:12,one:12,onli:[6,12],op_exp:8,oper:[5,8,12],option:[1,5,6,7,8,9],orig_d:6,orig_data:6,orig_seri:7,origin:12,other:[1,8,12],other_current_asset:1,other_current_liab:1,other_incom:1,other_lt_asset:1,other_lt_liab:1,other_op_exp:8,out:12,packag:[11,15],page:15,panda:[1,4,6,7,8,12],paramet:[3,4],part:1,particular:4,pass:[6,10,12],path:12,payabl:[1,12],pct_of:[1,6,8],pct_of_config:6,pct_of_seri:6,percentag:6,period:[3,4,6,12,16],pip:16,plant:[1,12],plot:[0,7,11,12],plot_forecast:6,port:1,portion:[1,12],possibl:12,ppe:1,practic:12,predict:[6,7,16],previous:12,primary_nam:9,prior_stat:[1,5,8],produc:12,profit:[8,12],project:0,properti:[1,3,4,5,6,7,8,9,12],prophet:[0,6],prophet_kwarg:[1,6,8],provis:8,purpos:12,python:[0,12,13],quarterli:7,rais:12,rang:12,rate:[12,16],rd_exp:8,reach:6,read_csv:12,read_excel:[1,3,8,16],rec:1,receiv:[1,12],recent:[0,6,16],recentvaluemodel:7,ref_dat:7,regress:[7,16],regressionresult:7,replac:[6,12],repres:6,research:8,result:[6,7,12],result_df:7,retain:[1,12],retained_earn:1,rev:8,revenu:[1,8,12],root_fold:12,run:6,runner:12,runtimewarn:12,sake:12,sale:[1,8,12],salesnon:1,same:12,script:12,search:15,see:[5,6,7,16],self:[5,6,7],sell:8,sep:12,separ:12,sequenc:[4,9],seri:[2,3,5,6,7],set:4,set_valu:4,sga:8,share:1,sharehold:1,sheet:[1,3,4,12,16],sheet_nam:10,shortterm:1,should:[5,6,12],signatur:[5,6,7],simpl:16,simpli:12,sinc:12,singl:[4,6],size:12,sold:[8,12],sourc:[0,1,2,3,4,5,6,7,8,9,10,12,13,15],sphinx:[12,13],st_debt:1,st_invest:1,standard:2,standardize_name_for_look_up:2,standardize_names_in_series_index:2,start:15,statement:[0,1,5,8,10,11,13,14,16],statement_cl:[1,5,8],statement_nam:[1,5,8],statementconfigmanag:4,statementsbas:[0,1,8,11],statementsconfigmanag:4,statsmodel:7,stderr:7,step:12,still:12,stmt:[3,12,16],stmts2:12,stock:[1,12],stockcommon:1,stockhold:[1,12],stocknet:1,stockrow:12,str:[2,3,4,5,6,7,9],submodul:[11,15],subpackag:[11,15],subset:[6,12],suitabl:12,support:6,sympi:4,sympy_namespac:4,t_offset:[4,5],tax:[1,8,12],tax_exp:8,tax_liab_lt:1,tax_liab_st:1,tca:1,term:[1,12],test:12,thei:12,thi:[3,6,12,16],those:12,through:12,time:[4,12],timestamp:[1,4,5,8],to_df:5,to_manu:[6,12],to_seri:[5,6],total:[1,8,12,14],total_asset:1,total_current_asset:1,total_current_liab:1,total_debt:[1,8,12],total_equ:1,total_liab:1,total_liab_and_equ:1,total_non_current_asset:1,total_non_current_liab:1,trend:[0,6,12,16],true_divid:12,tutori:15,type:[1,2,3,4,5,6,7,8,9,10,12],union:[1,4,5,6,8,9],unusu:8,updat:[4,12],update_al:[4,12],usag:15,use:[4,12],use_level:[6,12],used:[5,12],userwarn:12,using:[12,13],usual:[1,8,12],valu:[4,12,16],values_dict:4,variabl:[3,4],versu:7,via:[12,16],wai:[1,8,12],warn:12,web:12,well:4,where:12,whether:6,which:[10,12],wmt:[1,3,8,16],work:[0,12],would:3,write:8,writedown:8,xlabel:[6,7],xlsx:[1,3,8,16],y_0:12,ylabel:[6,7],you:12,your:12,zip:13},titles:["finstmt package","finstmt.bs package","finstmt.clean package","finstmt.combined package","finstmt.config_manage package","finstmt.findata package","finstmt.forecast package","finstmt.forecast.models package","finstmt.inc package","finstmt.items package","finstmt.loaders package","finstmt","Forecasting Financial Statements with <code class=\"docutils literal notranslate\"><span class=\"pre\">finstmt</span></code>","Examples","Computation times","Welcome to finstmt documentation!","Getting started with finstmt"],titleterms:{"default":12,adjust:12,assumpt:12,averag:7,base:[4,7],cagr:7,capiq:10,chang:12,chooser:7,clean:2,combin:3,comput:14,config:[1,6,8,9],config_manag:4,copi:12,data:[1,4,8],databas:5,datafram:6,document:15,exampl:13,exc:0,exist:12,financi:12,findata:5,finstmt:[0,1,2,3,4,5,6,7,8,9,10,11,12,15,16],first:12,forecast:[6,7,12,16],get:16,global_:4,inc:8,indic:15,instal:16,item:9,link:15,load:12,loader:10,logger:0,main:[1,6,8],manual:7,method:12,model:7,modul:[0,1,2,3,4,5,6,7,8,9,10],name:2,overview:15,packag:[0,1,2,3,4,5,6,7,8,9,10],plot:6,prophet:7,quick:15,recent:7,run:12,second:12,set:12,start:16,statement:[3,4,6,12],statementsbas:5,submodul:[0,1,2,3,4,5,6,7,8,9,10],subpackag:[0,6],tabl:15,time:14,trend:7,usag:16,view:12,welcom:15}})