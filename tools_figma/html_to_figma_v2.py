#!/usr/bin/env python3
"""
HTML to Figma JSON Converter (无依赖版本)
批量转换科技厅原型HTML为Figma可导入的JSON格式
"""

import os
import re
import json
from pathlib import Path

class HTMLToFigmaConverter:
    def __init__(self):
        self.color_map = {
            '#1890ff': {'r': 0.094, 'g': 0.565, 'b': 1},      # 蓝色
            '#52c41a': {'r': 0.322, 'g': 0.769, 'b': 0.102},  # 绿色
            '#fa8c16': {'r': 0.98, 'g': 0.549, 'b': 0.086},  # 橙色
            '#ff4d4f': {'r': 1, 'g': 0.302, 'b': 0.310},      # 红色
            '#2c2c2c': {'r': 0.173, 'g': 0.173, 'b': 0.173},  # 深色菜单背景
            '#1a1a1a': {'r': 0.102, 'g': 0.102, 'b': 0.102},  # 子菜单背景
            '#f0f2f5': {'r': 0.941, 'g': 0.949, 'b': 0.961},  # 页面背景
            '#ffffff': {'r': 1, 'g': 1, 'b': 1},              # 白色
            '#333333': {'r': 0.2, 'g': 0.2, 'b': 0.2},        # 文字深色
            '#666666': {'r': 0.4, 'g': 0.4, 'b': 0.4},        # 文字中灰
            '#999999': {'r': 0.6, 'g': 0.6, 'b': 0.6},        # 文字浅灰
            '#dddddd': {'r': 0.867, 'g': 0.867, 'b': 0.867},  # 边框
            '#fafafa': {'r': 0.98, 'g': 0.98, 'b': 0.98},     # 表头背景
            '#3a3a3a': {'r': 0.227, 'g': 0.227, 'b': 0.227},  # 菜单hover
            '#b8b8b8': {'r': 0.722, 'g': 0.722, 'b': 0.722},  # 菜单文字
        }
        self.page_width = 1440
        self.page_height = 1024
        self.sidebar_width = 220
        
    def create_text_node(self, name, x, y, text, font_size=13, color=None, bold=False, width=None):
        """创建文本节点"""
        if color is None:
            color = {'r': 0.2, 'g': 0.2, 'b': 0.2}
        
        font_name = {'family': 'PingFang SC', 'style': 'Bold' if bold else 'Regular'}
        
        if width is None:
            width = len(text) * font_size * 0.8
        
        return {
            'name': name,
            'type': 'TEXT',
            'x': x,
            'y': y,
            'width': width,
            'height': font_size + 4,
            'characters': text,
            'fontSize': font_size,
            'fontName': font_name,
            'fills': [{'type': 'SOLID', 'color': color}]
        }
    
    def create_frame_node(self, name, x, y, width, height, fill_color=None, stroke_color=None, corner_radius=0):
        """创建框架节点"""
        node = {
            'name': name,
            'type': 'FRAME',
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'children': []
        }
        
        if fill_color:
            node['fills'] = [{'type': 'SOLID', 'color': fill_color}]
        
        if stroke_color:
            node['strokes'] = [{'type': 'SOLID', 'color': stroke_color}]
            node['strokeWeight'] = 1
        
        if corner_radius > 0:
            node['cornerRadius'] = corner_radius
            
        return node
    
    def create_button_node(self, name, x, y, text, bg_color, text_color=None):
        """创建按钮节点"""
        if text_color is None:
            text_color = {'r': 1, 'g': 1, 'b': 1}
        
        btn_width = len(text) * 13 + 24
        btn_height = 28
        
        button = self.create_frame_node(name, x, y, btn_width, btn_height, bg_color, corner_radius=3)
        text_node = self.create_text_node(text, 12, 5, text, 12, text_color)
        button['children'].append(text_node)
        
        return button
    
    def parse_title(self, html_content):
        """解析HTML标题"""
        match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
        if match:
            title = match.group(1).strip()
            title = title.replace(' - 主管单位', '').strip()
            return title
        return '未命名页面'
    
    def create_sidebar(self):
        """创建左侧菜单栏"""
        sidebar = self.create_frame_node(
            '左侧菜单栏', 0, 0, self.sidebar_width, self.page_height,
            self.color_map['#2c2c2c']
        )
        
        # Logo区域
        logo = self.create_text_node('Logo', 20, 20, '大型科学仪器管理平台', 16, {'r': 1, 'g': 1, 'b': 1}, bold=True, width=180)
        sidebar['children'].append(logo)
        
        # 分割线
        divider = self.create_frame_node('分割线', 0, 60, self.sidebar_width, 1, self.color_map['#3a3a3a'])
        sidebar['children'].append(divider)
        
        # 菜单项
        menu_items = [
            ('首页', False),
            ('仪器管理', True),
            ('服务管理', False),
            ('机构管理', False),
            ('奖补管理', False),
            ('用户管理', False),
            ('系统管理', False),
        ]
        
        y_pos = 70
        for item_name, is_active in menu_items:
            bg_color = self.color_map['#1890ff'] if is_active else None
            text_color = {'r': 1, 'g': 1, 'b': 1} if is_active else self.color_map['#b8b8b8']
            
            menu_item = self.create_frame_node(f'菜单-{item_name}', 0, y_pos, self.sidebar_width, 48, bg_color)
            menu_text = self.create_text_node(item_name, 20, 14, item_name, 14, text_color)
            menu_item['children'].append(menu_text)
            sidebar['children'].append(menu_item)
            
            y_pos += 48
        
        return sidebar
    
    def create_search_card(self):
        """创建搜索卡片"""
        card = self.create_frame_node(
            '搜索卡片', 24, 68, 1172, 120,
            self.color_map['#ffffff'],
            self.color_map['#dddddd']
        )
        
        # 搜索条件标签
        labels = ['仪器名称', '仪器型号', '所属单位', '仪器分类', '状态']
        x_pos = 20
        for label in labels:
            label_text = self.create_text_node(f'标签-{label}', x_pos, 20, label + '：', 13, {'r': 0.4, 'g': 0.4, 'b': 0.4})
            card['children'].append(label_text)
            
            # 输入框背景
            input_bg = self.create_frame_node(f'输入框-{label}', x_pos + 60, 15, 150, 32, self.color_map['#ffffff'], self.color_map['#dddddd'])
            card['children'].append(input_bg)
            
            x_pos += 230
        
        # 查询按钮
        btn = self.create_button_node('查询按钮', 1020, 70, '查询', self.color_map['#1890ff'])
        card['children'].append(btn)
        
        # 重置按钮
        reset_btn = self.create_button_node('重置按钮', 1090, 70, '重置', self.color_map['#ffffff'], {'r': 0.4, 'g': 0.4, 'b': 0.4})
        card['children'].append(reset_btn)
        
        return card
    
    def create_table(self, page_name):
        """创建数据表格"""
        table = self.create_frame_node(
            '数据表格', 24, 208, 1172, 500,
            self.color_map['#ffffff'],
            self.color_map['#dddddd']
        )
        
        # 表头
        header = self.create_frame_node('表头', 0, 0, 1172, 48, self.color_map['#fafafa'])
        headers = ['序号', '仪器名称', '仪器型号', '所属单位', '仪器分类', '购置金额', '状态', '操作']
        x_pos = 15
        col_widths = [50, 150, 120, 150, 100, 100, 80, 200]
        
        for i, h in enumerate(headers):
            h_text = self.create_text_node(f'表头-{h}', x_pos, 14, h, 13, {'r': 0.2, 'g': 0.2, 'b': 0.2})
            header['children'].append(h_text)
            x_pos += col_widths[i]
        table['children'].append(header)
        
        # 数据行示例
        for row_idx in range(3):
            y_offset = 60 + row_idx * 50
            
            # 行数据
            row_data = [str(row_idx + 1), '高分辨质谱仪', 'Q-Exactive', '湖南大学', '分析仪器', '280万', '正常']
            x_pos = 15
            for i, cell in enumerate(row_data):
                cell_text = self.create_text_node(f'单元格-{row_idx}-{i}', x_pos, y_offset + 14, cell, 13)
                table['children'].append(cell_text)
                x_pos += col_widths[i]
            
            # 操作按钮
            view_btn = self.create_button_node(f'查看-{row_idx}', 990, y_offset + 10, '查看', self.color_map['#1890ff'])
            edit_btn = self.create_button_node(f'编辑-{row_idx}', 1045, y_offset + 10, '编辑', self.color_map['#fa8c16'])
            del_btn = self.create_button_node(f'删除-{row_idx}', 1100, y_offset + 10, '删除', self.color_map['#ff4d4f'])
            
            table['children'].extend([view_btn, edit_btn, del_btn])
        
        return table
    
    def create_stats_cards(self):
        """创建统计卡片（首页用）"""
        stats_container = self.create_frame_node('统计卡片区', 24, 68, 1172, 120)
        
        stats = [
            ('128', '仪器总数'),
            ('86', '正常'),
            ('32', '维护中'),
            ('10', '报废'),
        ]
        
        x_pos = 0
        for value, label in stats:
            card = self.create_frame_node(
                f'统计-{label}', x_pos, 0, 270, 120,
                self.color_map['#ffffff'],
                None, 4
            )
            
            value_text = self.create_text_node(f'数值-{label}', 0, 30, value, 36, self.color_map['#1890ff'], bold=True, width=270)
            label_text = self.create_text_node(f'标签-{label}', 0, 80, label, 14, {'r': 0.4, 'g': 0.4, 'b': 0.4}, width=270)
            
            card['children'].extend([value_text, label_text])
            stats_container['children'].append(card)
            x_pos += 290
        
        return stats_container
    
    def convert_file(self, html_path):
        """转换单个HTML文件"""
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 获取标题
        title = self.parse_title(html_content)
        file_name = Path(html_path).stem
        
        # 创建页面Frame
        page_frame = self.create_frame_node(
            f'Desktop - {title}',
            0, 0, self.page_width, self.page_height,
            self.color_map['#f0f2f5']
        )
        
        # 添加左侧菜单
        sidebar = self.create_sidebar()
        page_frame['children'].append(sidebar)
        
        # 添加主内容区背景
        main_content = self.create_frame_node(
            '主内容区', self.sidebar_width, 0,
            self.page_width - self.sidebar_width, self.page_height,
            self.color_map['#f0f2f5']
        )
        
        # 页面标题
        page_title = self.create_text_node('页面标题', 24, 24, title, 18, {'r': 0.2, 'g': 0.2, 'b': 0.2}, bold=True)
        main_content['children'].append(page_title)
        
        # 根据页面类型决定内容
        if '首页' in file_name or '主管单位' == file_name:
            # 首页显示统计卡片
            stats = self.create_stats_cards()
            main_content['children'].append(stats)
        else:
            # 其他页面显示搜索和表格
            search_card = self.create_search_card()
            main_content['children'].append(search_card)
            
            table = self.create_table(title)
            main_content['children'].append(table)
        
        page_frame['children'].append(main_content)
        
        return {
            'name': title,
            'type': 'PAGE',
            'children': [page_frame]
        }
    
    def convert_all(self, source_dir, output_file):
        """批量转换所有HTML文件"""
        html_files = sorted(Path(source_dir).glob('*.html'))
        
        document = {
            'name': '科技厅原型-主管单位系统',
            'type': 'DOCUMENT',
            'children': []
        }
        
        print(f'开始转换 {len(html_files)} 个HTML文件...')
        
        for i, html_path in enumerate(html_files, 1):
            try:
                page = self.convert_file(html_path)
                document['children'].append(page)
                print(f'[{i}/{len(html_files)}] ✓ {html_path.name}')
            except Exception as e:
                print(f'[{i}/{len(html_files)}] ✗ {html_path.name}: {e}')
        
        # 保存JSON文件
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({'document': document}, f, ensure_ascii=False, indent=2)
        
        print(f'\n转换完成！')
        print(f'输出文件: {output_file}')
        print(f'总页数: {len(document["children"])}')
        
        # 返回统计信息
        return {
            'total_files': len(html_files),
            'converted': len(document['children']),
            'output_file': output_file
        }

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print('用法: python html_to_figma.py <source_dir> <output.json>')
        sys.exit(1)
    
    source_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    converter = HTMLToFigmaConverter()
    result = converter.convert_all(source_dir, output_file)
