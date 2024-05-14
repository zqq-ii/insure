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

SELECT * FROM ord_proposal where proposal_no ='ET202400028643000181';

-- 通过投保单号删除保单信息

DELETE FROM ord_proposal where proposal_no ='EP202403640077372178';

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

SELECT * FROM `insure_v1`.`subject_matter_info`;

-- 门店保,营业执照

SELECT * FROM `insure_v1`.`ord_insured_extra` ORDER BY id DESC;

-- 门店保,支付凭证,通过保单号查询

SELECT * FROM `insure_v1`.`pay_certificate` WHERE ray_code = 'ET202400028972000181';

-- 门店保,发票申请记录

SELECT * FROM `insure_v1`.`policy_invoice`;

SELECT * FROM `insure_v1`.`policy_invoice`;
