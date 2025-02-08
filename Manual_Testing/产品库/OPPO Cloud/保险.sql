-- 通过经济系统团单号查询保单信息

SELECT * FROM ord_proposal where group_channel_proposal_no ='G8551881834607706891';

DELETE FROM ord_proposal where group_channel_proposal_no ='G8551881834607706863';

-- 通过团单号查询保单信息

SELECT * FROM ord_proposal where group_proposal_no ='5H2405DA1A2K2D8';

SELECT * FROM ord_proposal where group_proposal_no ='8H2405DA1A3Y868';

-- 通过保单号查询保单信息

SELECT * FROM ord_proposal where policy_no ='EP202404251054866663';

-- 通过保单号查询分期表信息

SELECT * FROM ord_policy_installment where policy_no ='P10E120240101V0014502';

-- 通过保单号查询支付退费信息

SELECT * FROM pay_pay_refund_detail_sale_platform WHERE policy_no = 'P10E120240101V0014531';

-- 通过保单号删除保单信息

DELETE FROM ord_correct_order WHERE policy_no = '6H2405DA88T3926';

-- 通过投保单号查询保单信息

SELECT * FROM ord_proposal where proposal_no ='ET202400029370000181';

-- 通过投保单号删除保单信息

DELETE FROM ord_proposal where proposal_no ='ET202400029352000181';

-- 通过保单号查询,团单,脱保,退运险执行定时任务后数据写入

SELECT * FROM asy_task where identification = 'EP202403202280000123';

 -- 通过保单号查询保额批增信息

SELECT * FROM increase_amount_record where policy_no = '6H2405DA88T0696';

-- 通过投保单号查询手机1imei

select t2.* from ord_proposal t1
left join ord_electronics t2
on t1.id = t2.proposal_id
where t1.proposal_no = 'I8634358366467153931';

-- 通过出单时间和产品计划码查询改时间端保单信息

SELECT * FROM insure_v1.ord_proposal  WHERE plan_code ='TKG20240325F04' AND create_time>'2024-04-9 00:00:00' and create_time <= '2024-04-10 00:00:00'
 -- AND status IN (4,5) AND policy_no =''
ORDER BY id ASC;

-- 通过保单号查询手机理赔申请记录 :1-已接收、2-申请成功、3-申请失败、4 - 申请中

SELECT * FROM claim_apply_record WHERE policy_no = 'EP202403640000019695';

-- 通过保单号查询理赔材料上传信息;upload_status上传状态：1 - 不可上传、2 - 可上传、3 - 上传成功 、 4 - 上传失败、 5 - 处理中;async_type1 - 同步、2 - 异步

SELECT * FROM claim_material WHERE policy_no = 'EP202403640000019695';

-- 退运险理赔申请记录,通过保单号查询

select * from claim_apply_freight_detail WHERE policy_no = 'PLE220234403QA00A00006';

-- 退运险订单表,通过保单号查询

select * from claim_apply_record WHERE policy_no = 'PLE220234403QA00A00004';

-- 通过承保单号查询直付签约表

SELECT * FROM policy_freight_order WHERE policy_no = 'PLE220234403QA00A00004';

-- 通过保单号查询保单url

SELECT * FROM ord_policy_electronic where policy_no ='H231226443292400192621';

-- 错误映射信息

SELECT * FROM `insure_channel_v1`.`channel_error_map`;

INSERT INTO `insure_channel_v1`.`channel_error_map` (error_code, channel_error_code,match_error_message)
VALUES ('100_UDG_S76', '1005','fail--根据您的投保申请，经我司风险评估后，需要进一步审核。若您有就医就诊情况，建议您提前准备门诊、出院小结或者住院病历首页等病历资料'),
('100_UDG_S76', '1005','fail--尊敬的顾客您好，我们抱歉的通知您，您的本次投保未通过审核，建议您选择我司其他产品，感谢您的支持与理解'),
('100_UDG_S76', '1005','fail--尊敬的顾客您好，本次申请和以前在我司投保的累计保险金额已超过限额（可投保保额：-3.00万元），您可以调整保险金额或者选择我司其他产品，感谢您的支持与理解'),
('100_UDG_S76', '1005','fail--尊敬的顾客您好，我们抱歉的通知您，您的本次投保未通过我司风险评估，感谢您关注泰康在线'),
('100_UDG_S76', '1005','fail--尊敬的客户很抱歉，根据我公司核保模型综合评估，暂不支持您投保此产品，您可以自助选择我司其他产品。感谢您的支持与理解！'),
('100_UDG_S18', '1005','fail--投保人姓名格式不正确,符号只能出现在两个汉字或两个字母之间'),
('100_UDG_S18', '1005','fail--投保人姓名格式不正确,符号只能出现在两个汉字或两个字母之间'),
('100_UDG_S17', '1005','fail--姓名格式不正确,请检查报文'),
('100_UDG_P06', '1005','fail--未匹配到相应的保费，请核实');

UPDATE `insure_channel_v1`.`channel_error_map` SET channel_error_text='经济公司映射保司错误: 姓名格式不正确,请检查报文!' WHERE id = 8;

-- 错误信息关联产品计划方案

SELECT * FROM `insure_channel_v1`.`channel_plan_error` ;

INSERT INTO `insure_channel_v1`.`channel_plan_error` (error_id,plan_id)
VALUES (1,26 ),(2,26 ),(3,26 ),(4,26 ),(5,26 ),(6,26 ),(7,26 ),(8,26 ),(9,26 ),
(1,27 ),(2,27 ),(3,27 ),(4,27 ),(5,27 ),(6,27 ),(7,27 ),(8,27 ),(9,27 ),
(1,28 ),(2,28 ),(3,28 ),(4,28 ),(5,28 ),(6,28 ),(7,28 ),(8,28 ),(9,28 ),
(1,31 ),(2,31 ),(3,31 ),(4,31 ),(5,31 ),(6,31 ),(7,31 ),(8,31 ),(9,31 ),
(1,40 ),(2,40 ),(3,40 ),(4,40 ),(5,40 ),(6,40 ),(7,40 ),(8,40 ),(9,40 ),
(1,41 ),(2,41 ),(3,41 ),(4,41 ),(5,41 ),(6,41 ),(7,41 ),(8,41 ),(9,41 ),
(1,44 ),(2,44 ),(3,44 ),(4,44 ),(5,44 ),(6,44 ),(7,44 ),(8,44 ),(9,44 ),
(1,45 ),(2,45 ),(3,45 ),(4,45 ),(5,45 ),(6,45 ),(7,45 ),(8,45 ),(9,45 );

-- 产品计划,方案表

SELECT * FROM `insure_channel_v1`.`channel_plan` ;

-- 门店保,标的信息

SELECT * FROM `insure_v1`.`subject_matter_info` ORDER BY id DESC;

-- 门店保,营业执照

SELECT * FROM `insure_v1`.`ord_insured_extra` ORDER BY id DESC;

-- 门店保,支付凭证,通过保单号查询

SELECT * FROM `insure_v1`.`pay_certificate` WHERE ray_code = 'ET202400029354000181';

-- 门店保,发票申请记录,通过保单号查询

SELECT * FROM `insure_v1`.`policy_invoice` WHERE policy_no = 'EP202403202635000123';

-- 新的2024.12.17

--根据保单号查询保单表：

select * from ord_proposal where policy_no='IH1100014772864305'

根据保单状态倒序排序：

select * from ord_proposal where status='5' ORDER BY id ASC limit 100



根据产品计划码和状态查询保单：

select * from ord_proposal where plan_code='ZAN2024110701' and status='5'


根据承保单号查询保单表：

select * from ord_proposal where proposal_no='PA157EE241125298303346'


根据续保原保单号查询保单表：

select * from ord_proposal where original_policy_no='IH1100014746375059'


根据业务单号查询保单：

select * from ord_proposal where business_no='B9218996358550283474'


修改年缴保单时间：

UPDATE ord_proposal set effective_time='2024-10-25 00:00:00', expire_time='2025-10-24 23:59:59' where policy_no='PI07306241125213616383'


修改保单生效时间：

UPDATE ord_proposal set effective_time='2024-09-01 00:00:00' where policy_no='H240902002917830140852'


修改保单承保时间：

UPDATE ord_proposal set accept_time='2024-09-01 00:00:00' where policy_no='H240902002917830140852'


修改保单号创建时间：

UPDATE ord_proposal set create_time='2024-09-02 00:00:00' where policy_no='EP202404251054866661'


修改保单状态：

UPDATE ord_proposal set status='5' where policy_no='H241114003925970184243'


修改保单号：

UPDATE ord_proposal set policy_no='9641789921' where business_no='B8726695146813417125'


删除保单：

DELETE FROM ord_proposal WHERE policy_no='PLE220244403QX00A10104'


根据保单状态和计划码查询保单：

select * from ord_proposal where product_code='TP20220318' and status='5' order by id desc


签约记录表：

select * from sign_record where trans_serial_no='8866396551629367878'


select * from sign_record ORDER BY update_time desc


账户信息表：

select * from account_info


签约用户信息表：

select * from sign_user_info


转入申请表：

select * from transfer_order where order_no='O272320210324105142682' and order_type='1'


select * from transfer_order where transfer_order_no='O8884212625729055481' and order_type='1'


转出申请表：

select * from transfer_order where order_no='O272320210324105142682' and order_type='2'


根据保单号查询收益：

select * from income_info WHERE policy_no='86000020211600336422'


根据保单号查询收益：

select * from income_info WHERE policy_no='86000020211600336422' ORDER BY update_time desc


根据保单号查询净值收益：

select * from net_value_yield where account_code='AC0012' and net_date='2024-07-19 00:00:00' ORDER BY update_time desc


查询日保有量文件表：

select * from turn_over_info ORDER BY create_time desc



查询贷款信息表：

select * from loan_info where policy_no='86000020211600336422'



分期表：

select * from ord_policy_installment where policy_no='PI07306241125213616383'



通过保单号和分期期数修改分期截至时间：

UPDATE ord_policy_installment set pay_deadline_time='2024-11-24 23:59:59' where policy_no='PI07306241125213616383' and installment_num='2'



分期表倒序：

select * from ord_policy_installment order by id desc



修改月缴分期状态和退费金额：

UPDATE ord_policy_installment set refund_premium='0',status='1' where policy_no='IH1100014769848138'and installment_num in (2,3,4,5,6,7,8,9,10,11,12)



修改月缴到期月缴时间：

UPDATE ord_policy_installment set pay_deadline_time='2024-11-04' where policy_no='PI157EE241125175658732' and installment_num='4'



修改年缴分期状态和退费金额：

UPDATE ord_policy_installment set refund_premium='0',status='1' where policy_no='PI07306241125213616383' and installment_num='1'



修改年缴分期时间：

UPDATE ord_policy_installment set start_time='2024-11-25 00:00:00',end_time='2024-12-24 23:59:59'where policy_no='PI07306241125213616383' and installment_num='2'



select * from ord_contract where proposal_no in('P00420320240802234866788283264')



回调记录表：

select * from callback_data_records where identification='P10E120240101V0024303'



统一异步任务表：

select * from asy_task where identification='6H2405DA9NC1A06'



select * from asy_task where identification in('1132352024433','CH00000002874618')



select * from ord_contract where proposal_no in('P00420320240802234866788283264')



select * from asy_task order by id desc;



手机表产品类型：

select * from ord_electronics where proposal_id='0201'



根据保单号查询报案记录：

select * from claim_apply_record where policy_no='IH1100014772993186'



根据报案号查询报案记录：

select * from claim_apply_record where report_no='07P20212912024000160'



删除报案数据：

DELETE FROM claim_apply_record WHERE report_no='07P20212912024000159'



根据报案号查询影像：

select * from claim_material where report_no='CN07306241100045295338'



根据保单号查询影像：

select * from claim_material where policy_no='PI07306241125212399458'



根据时间段查询影响：

select * from claim_material where create_time > 20241122000000



根据报案号修改状态：

UPDATE claim_material SET upload_status='3' where report_no='CN07306241100045295130'



根据保单号修改报案状态：

UPDATE claim_material SET upload_status='3' where policy_no='PI07306241125172643158'



通过保单号查询手机理赔申请记录:

SELECT * FROM claim_material WHERE policy_no = 'PI07306241125213614101'



通过投保单号查询手机1imei:

select t2.* from ord_proposal t1 left join ord_electronics t2 on t1.id = t2.proposal_id where t1.proposal_no = 'PI07306241125211949032'



查询手机1imei：

select * from ord_electronics where proposal_id='50116'



通过产品序列号查询手机limei:

select * from ord_electronics where product_serial_no='ZIDING3DZDQ8LGZWTQR7VBI87TPR8O8O'



修改手机1imei：

UPDATE ord_electronics set product_serial_no='2024092400000012' where proposal_id='27233'



通过保单查询电子保单表：

select * from ord_policy_electronic where policy_no='PI07306241125207291079'



通过保单号查询支付结果：

select * from pay_pay_refund_detail_sale_platform where policy_no='IH1100014769708859'



通过销售平台订单号查询支付退费接口：

select * from pay_pay_refund_detail_sale_platform where sale_platform_order_no='ZIDINGV2FCV75JT3J960GTOKIHE97PTC'



根据报案号查询账户信息：

select * from claim_account_info where report_no='CL0300003391509393'



根据报案号查询附件信息：

select * from claim_attachment_info where report_no='CL0300003391509393'



根据保单号查询报案记录：

select * from claim_apply_record where report_no='CL0300003391516646'



根据保单号查询保单表：

select * from ord_proposal where policy_no='IH1100014768954451'



报案回调记录表：

select * from case_status_push_data where policy_no='IH1100014770101222'



删除回调记录表：

DELETE FROM case_status_push_data















