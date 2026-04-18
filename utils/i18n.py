# utils/i18n.py

"""Internationalization support."""
import locale
import os
import platform
from typing import Dict

class Translator:
    """Simple translation system for multilingual support."""
    
    def _detect_system_language(self):
        """Detect system language with better Windows support."""
        # Method 1: Check environment variables first
        for env_var in ['LANG', 'LANGUAGE', 'LC_ALL', 'LC_MESSAGES']:
            lang = os.environ.get(env_var)
            if lang:
                lang = lang.lower()
                if lang.startswith('de'):
                    return 'de'
                if lang.startswith('ru'):
                    return 'ru'
        
        # Method 2: Use locale.getlocale() (more reliable than getdefaultlocale)
        try:
            current_locale = locale.getlocale()
            if current_locale[0]:
                locale_code = current_locale[0].lower()
                if locale_code.startswith('de'):
                    return 'de'
                if locale_code.startswith('ru'):
                    return 'ru'
        except:
            pass
        
        # Method 3: Windows-specific detection
        if platform.system() == 'Windows':
            try:
                import ctypes
                # Get Windows locale ID
                lcid = ctypes.windll.kernel32.GetUserDefaultLCID()
                # German locales have LCID starting with 0x04 (like 0x0407 for de-DE)
                if (lcid & 0xFF) == 0x07:  # German primary language
                    return 'de'
                if (lcid & 0xFF) == 0x19:  # Russian primary language
                    return 'ru'
            except:
                pass
        
        # Method 4: Fallback to getdefaultlocale() if nothing else works
        try:
            system_lang = locale.getdefaultlocale()[0]
            if system_lang:
                system_lang = system_lang.lower()
                if system_lang.startswith('de'):
                    return 'de'
                if system_lang.startswith('ru'):
                    return 'ru'
        except:
            pass
        
        return 'ru'  # Default fallback

    def __init__(self):
        """Initialize translator with improved locale detection."""
        self.current_lang = 'ru'
        self.translations = {
            
                'en': {
                    # Main Interface
                    'app_title': 'Universal File Search & Index Tool',
                    'search_tab': 'Search Files',
                    'manage_tab': 'Manage Indices',
                    'duplicates_tab': 'Find Duplicates',
                    'settings_tab': 'Settings',
                    
                    # Search Interface
                    'search_criteria': 'Search Criteria',
                    'name_pattern': 'Name (regex):',
                    'name_examples': 'Examples: *.jpg, IMG_\\d+, (?i)vacation',
                    'size_range': 'Size range:',
                    'size_examples': ' (e.g., 1MB, 500KB)',
                    'date_range': 'Date range:',
                    'date_examples': ' (YYYY-MM-DD or \'today\', \'yesterday\')',
                    'search_button': 'Search Files',
                    'clear_button': 'Clear',
                    'search_results': 'Search Results',
                    'filename_col': 'Filename',
                    'size_col': 'Size',
                    'modified_col': 'Modified',
                    'path_col': 'Full Path',
                    'open_file': 'Open File',
                    'open_folder': 'Open Folder',
                    'copy_path': 'Copy Path',
                    'export_results': 'Export Results',
                    'close_button': 'Close',
                    
                    # Index Management
                    'index_catalog': 'Index Catalog',
                    'available_indices': 'Available Indices',
                    'create_index': 'Create New Index',
                    'refresh_indices': 'Refresh List',
                    'delete_index': 'Delete Selected',
                    'index_info': 'Index Information',
                    'root_path': 'Root Path:',
                    'file_count': 'Files:',
                    'total_size': 'Total Size:',
                    'created_date': 'Created:',
                    'hash_method': 'Hash Method:',
                    
                    # Duplicate Detection
                    'source_folder': 'Source Folder',
                    'destination_folders': 'Destination Folders',
                    'browse_button': 'Browse...',
                    'add_folder': 'Add Folder',
                    'remove_selected': 'Remove Selected',
                    'clear_all': 'Clear All',
                    'options': 'Options',
                    'use_hash': 'Use file hashes for comparison',
                    'reuse_indices': 'Reuse existing indices',
                    'force_recreation': 'Force recreation of indices',
                    'start_scan': 'Start Scan',
                    'new_scan': 'New Scan',
                    'exit_button': 'Exit',

                    'method': 'Method',
                    'found': 'Found',
                    'files_with_duplicates': 'files with duplicates',
                    'total_size': 'Total Size',
                    
                    # Results and Actions
                    'duplicate_manager': 'Duplicate File Manager',
                    'information': 'Information',
                    'filter': 'Filter',
                    'regex_filter': 'Regex filter:',
                    'select_all_filtered': 'Select All Filtered',
                    'deselect_all': 'Deselect All',
                    'delete_selected': 'Delete Selected Files',
                    'generate_script': 'Generate Script...',
                    'index_col': 'Index',
                    
                    # Progress
                    'initializing': 'Initializing...',
                    'scanning_files': 'Scanning files...',
                    'building_index': 'Building index...',
                    'finding_duplicates': 'Finding duplicates...',
                    'cancel_button': 'Cancel',
                    
                    # Messages
                    'no_results': 'No search results to export.',
                    'export_complete': 'Results exported to:\n{}',
                    'export_error': 'Failed to export results:\n{}',
                    'search_error': 'Search failed:\n{}',
                    'no_duplicates': 'No duplicate files were found.\n\nWould you like to start a new scan?',
                    'confirm_deletion': 'Are you sure you want to permanently delete {} files ({})?\n\nThis action CANNOT be undone.',
                    'deletion_complete': 'Successfully deleted {} of {} selected files.',
                    'script_generated': 'Deletion script was successfully saved to:\n{}',
                    'ready_status': 'Ready to search {} indexed locations',
                    'searching_status': 'Searching...',
                    'found_status': 'Found {} files matching criteria',
                    'selected_status': 'Selected: {} files ({:.1f} MB)',
                    'no_selection_status': 'No files selected',
                    'path_copied': 'Copied path to clipboard: {}',
                    'select_source': 'Please select a source folder',
                    'select_dest': 'Please add at least one destination folder',
                    
                    # Settings
                    'language': 'Language:',
                    'default_hash': 'Default Hash Algorithm:',
                    'auto_load_indices': 'Auto-load indices on startup',
                    'index_locations': 'Index Search Locations:',
                    'add_location': 'Add Location',
                    'remove_location': 'Remove Location',
                    'apply_settings': 'Apply Settings',
                    
                    # Errors
                    'error': 'Error',
                    'file_not_found': 'File no longer exists:\n{}',
                    'invalid_regex': 'Invalid regex pattern: {}',
                    'invalid_size': 'Invalid size format: {}',
                    'invalid_date': 'Invalid date format: {}',
                    'scan_failed': 'Scan failed:\n{}',
                    'no_indices': 'No search indices found.',
                    'no_selection': 'No files are selected.',
                    'duplicate_folder': 'This folder is already in the list.',
                },
                
                'de': {
                    # Main Interface
                    'app_title': 'Universelles Datei-Such- & Index-Tool',
                    'search_tab': 'Dateien suchen',
                    'manage_tab': 'Indices verwalten',
                    'duplicates_tab': 'Duplikate finden',
                    'settings_tab': 'Einstellungen',
                    
                    # Search Interface
                    'search_criteria': 'Suchkriterien',
                    'name_pattern': 'Name (regex):',
                    'name_examples': 'Beispiele: *.jpg, IMG_\\d+, (?i)urlaub',
                    'size_range': 'Größenbereich:',
                    'size_examples': ' (z.B. 1MB, 500KB)',
                    'date_range': 'Datumsbereich:',
                    'date_examples': ' (JJJJ-MM-TT oder \'heute\', \'gestern\')',
                    'search_button': 'Dateien suchen',
                    'clear_button': 'Löschen',
                    'search_results': 'Suchergebnisse',
                    'filename_col': 'Dateiname',
                    'size_col': 'Größe',
                    'modified_col': 'Geändert',
                    'path_col': 'Vollständiger Pfad',
                    'open_file': 'Datei öffnen',
                    'open_folder': 'Ordner öffnen',
                    'copy_path': 'Pfad kopieren',
                    'export_results': 'Ergebnisse exportieren',
                    'close_button': 'Schließen',
                    
                    # Index Management
                    'index_catalog': 'Index-Katalog',
                    'available_indices': 'Verfügbare Indices',
                    'create_index': 'Neuen Index erstellen',
                    'refresh_indices': 'Liste aktualisieren',
                    'delete_index': 'Ausgewählte löschen',
                    'index_info': 'Index-Informationen',
                    'root_path': 'Stammpfad:',
                    'file_count': 'Dateien:',
                    'total_size': 'Gesamtgröße:',
                    'created_date': 'Erstellt:',
                    'hash_method': 'Hash-Methode:',
                    
                    # Duplicate Detection
                    'source_folder': 'Quellordner',
                    'destination_folders': 'Zielordner',
                    'browse_button': 'Durchsuchen...',
                    'add_folder': 'Ordner hinzufügen',
                    'remove_selected': 'Ausgewählte entfernen',
                    'clear_all': 'Alle löschen',
                    'options': 'Optionen',
                    'use_hash': 'Dateihashes für Vergleich verwenden',
                    'reuse_indices': 'Vorhandene Indices wiederverwenden',
                    'force_recreation': 'Neuerststellung der Indices erzwingen',
                    'start_scan': 'Scan starten',
                    'new_scan': 'Neuer Scan',
                    'exit_button': 'Beenden',

                    'method': 'Methode',
                    'found': 'Gefunden',
                    'files_with_duplicates': 'Dateien mit Duplikaten',
                    'total_size': 'Gesamtgröße',

                    'selected': 'Ausgewählt',
                    'source_duplicates': 'Quell-Duplikate',
                    'destination_duplicates': 'Ziel-Duplikate', 
                    'index_info': 'Index-Info',
                    'last_updated': 'Zuletzt aktualisiert',
                    'update_index': 'Index aktualisieren',
                    'multiple_indices_found': 'Mehrere Indices gefunden',
                    'select_indices_to_update': 'Wählen Sie zu aktualisierende Indices:',
                    
                    # Results and Actions
                    'duplicate_manager': 'Duplikat-Dateiverwaltung',
                    'information': 'Information',
                    'filter': 'Filter',
                    'regex_filter': 'Regex-Filter:',
                    'select_all_filtered': 'Alle gefilterten auswählen',
                    'deselect_all': 'Alle abwählen',
                    'delete_selected': 'Ausgewählte Dateien löschen',
                    'generate_script': 'Skript generieren...',
                    'index_col': 'Index',
                    
                    # Progress
                    'initializing': 'Initialisierung...',
                    'scanning_files': 'Scanne Dateien...',
                    'building_index': 'Erstelle Index...',
                    'finding_duplicates': 'Suche Duplikate...',
                    'cancel_button': 'Abbrechen',
                    
                    # Messages
                    'no_results': 'Keine Suchergebnisse zum Exportieren.',
                    'export_complete': 'Ergebnisse exportiert nach:\n{}',
                    'export_error': 'Fehler beim Exportieren der Ergebnisse:\n{}',
                    'search_error': 'Suche fehlgeschlagen:\n{}',
                    'no_duplicates': 'Keine doppelten Dateien gefunden.\n\nMöchten Sie einen neuen Scan starten?',
                    'confirm_deletion': 'Sind Sie sicher, dass Sie {} Dateien ({}) dauerhaft löschen möchten?\n\nDiese Aktion kann NICHT rückgängig gemacht werden.',
                    'deletion_complete': 'Erfolgreich {} von {} ausgewählten Dateien gelöscht.',
                    'script_generated': 'Löschskript wurde erfolgreich gespeichert unter:\n{}',
                    'ready_status': 'Bereit zum Durchsuchen von {} Indizes',
                    'searching_status': 'Suche läuft...',
                    'found_status': '{} Dateien gefunden, die den Kriterien entsprechen',
                    'selected_status': 'Ausgewählt: {} Dateien ({:.1f} MB)',
                    'no_selection_status': 'Keine Dateien ausgewählt',
                    'path_copied': 'Pfad in Zwischenablage kopiert: {}',
                    'select_source': 'Bitte wählen Sie einen Quellordner',
                    'select_dest': 'Bitte fügen Sie mindestens einen Zielordner hinzu',
                    
                    # Settings
                    'language': 'Sprache:',
                    'default_hash': 'Standard-Hash-Algorithmus:',
                    'auto_load_indices': 'Indices beim Start automatisch laden',
                    'index_locations': 'Index-Suchpfade:',
                    'add_location': 'Pfad hinzufügen',
                    'remove_location': 'Pfad entfernen',
                    'apply_settings': 'Einstellungen anwenden',
                    
                    # Errors
                    'error': 'Fehler',
                    'file_not_found': 'Datei existiert nicht mehr:\n{}',
                    'invalid_regex': 'Ungültiges Regex-Muster: {}',
                    'invalid_size': 'Ungültiges Größenformat: {}',
                    'invalid_date': 'Ungültiges Datumsformat: {}',
                    'scan_failed': 'Scan fehlgeschlagen:\n{}',
                    'no_indices': 'Keine Suchindices gefunden.',
                    'no_selection': 'Keine Dateien ausgewählt.',
                    'duplicate_folder': 'Dieser Ordner ist bereits in der Liste.',
                },

                'ru': {
                    # Main Interface
                    'app_title': 'Универсальный поиск и индексирование файлов',
                    'search_tab': 'Поиск файлов',
                    'manage_tab': 'Управление индексами',
                    'duplicates_tab': 'Поиск дубликатов',
                    'settings_tab': 'Настройки',

                    # Search Interface
                    'search_criteria': 'Критерии поиска',
                    'name_pattern': 'Имя (regex):',
                    'name_examples': 'Примеры: *.jpg, IMG_\\d+, (?i)отпуск',
                    'size_range': 'Диапазон размера:',
                    'size_examples': ' (например, 1MB, 500KB)',
                    'date_range': 'Диапазон даты:',
                    'date_examples': ' (YYYY-MM-DD или \'today\', \'yesterday\')',
                    'search_button': 'Искать файлы',
                    'clear_button': 'Очистить',
                    'search_results': 'Результаты поиска',
                    'filename_col': 'Имя файла',
                    'size_col': 'Размер',
                    'modified_col': 'Изменен',
                    'path_col': 'Полный путь',
                    'open_file': 'Открыть файл',
                    'open_folder': 'Открыть папку',
                    'copy_path': 'Копировать путь',
                    'export_results': 'Экспорт результатов',
                    'close_button': 'Закрыть',

                    # Index Management
                    'index_catalog': 'Каталог индексов',
                    'available_indices': 'Доступные индексы',
                    'create_index': 'Создать новый индекс',
                    'refresh_indices': 'Обновить список',
                    'delete_index': 'Удалить выбранный',
                    'index_info': 'Информация об индексе',
                    'root_path': 'Корневой путь:',
                    'file_count': 'Файлы:',
                    'total_size': 'Общий размер:',
                    'created_date': 'Создан:',
                    'hash_method': 'Метод хеширования:',

                    # Duplicate Detection
                    'source_folder': 'Исходная папка',
                    'destination_folders': 'Целевые папки',
                    'browse_button': 'Обзор...',
                    'add_folder': 'Добавить папку',
                    'remove_selected': 'Удалить выбранные',
                    'clear_all': 'Очистить все',
                    'options': 'Параметры',
                    'use_hash': 'Использовать хеши файлов для сравнения',
                    'reuse_indices': 'Повторно использовать существующие индексы',
                    'force_recreation': 'Принудительно пересоздать индексы',
                    'start_scan': 'Запустить сканирование',
                    'new_scan': 'Новое сканирование',
                    'exit_button': 'Выход',

                    'method': 'Метод',
                    'found': 'Найдено',
                    'files_with_duplicates': 'файлов с дубликатами',
                    'total_size': 'Общий размер',

                    'selected': 'Выбрано',
                    'source_duplicates': 'Дубликаты в источнике',
                    'destination_duplicates': 'Дубликаты в назначении',
                    'last_updated': 'Обновлен',
                    'update_index': 'Обновить индекс',
                    'multiple_indices_found': 'Найдено несколько индексов',
                    'select_indices_to_update': 'Выберите индексы для обновления:',

                    # Results and Actions
                    'duplicate_manager': 'Менеджер дубликатов',
                    'information': 'Информация',
                    'filter': 'Фильтр',
                    'regex_filter': 'Regex-фильтр:',
                    'select_all_filtered': 'Выбрать все отфильтрованные',
                    'deselect_all': 'Снять выделение',
                    'delete_selected': 'Удалить выбранные файлы',
                    'generate_script': 'Создать скрипт...',
                    'index_col': 'Индекс',

                    # Progress
                    'initializing': 'Инициализация...',
                    'scanning_files': 'Сканирование файлов...',
                    'building_index': 'Построение индекса...',
                    'finding_duplicates': 'Поиск дубликатов...',
                    'cancel_button': 'Отмена',

                    # Messages
                    'no_results': 'Нет результатов поиска для экспорта.',
                    'export_complete': 'Результаты экспортированы в:\n{}',
                    'export_error': 'Не удалось экспортировать результаты:\n{}',
                    'search_error': 'Поиск завершился ошибкой:\n{}',
                    'no_duplicates': 'Дубликаты файлов не найдены.\n\nХотите начать новое сканирование?',
                    'confirm_deletion': 'Вы уверены, что хотите навсегда удалить {} файлов ({})?\n\nЭто действие НЕЛЬЗЯ отменить.',
                    'deletion_complete': 'Успешно удалено {} из {} выбранных файлов.',
                    'script_generated': 'Скрипт удаления успешно сохранен в:\n{}',
                    'ready_status': 'Готово к поиску по {} индексированным расположениям',
                    'searching_status': 'Поиск...',
                    'found_status': 'Найдено {} файлов по заданным критериям',
                    'selected_status': 'Выбрано: {} файлов ({:.1f} MB)',
                    'no_selection_status': 'Файлы не выбраны',
                    'path_copied': 'Путь скопирован в буфер обмена: {}',
                    'select_source': 'Выберите исходную папку',
                    'select_dest': 'Добавьте хотя бы одну целевую папку',

                    # Settings
                    'language': 'Язык:',
                    'default_hash': 'Алгоритм хеширования по умолчанию:',
                    'auto_load_indices': 'Автозагрузка индексов при запуске',
                    'index_locations': 'Пути поиска индексов:',
                    'add_location': 'Добавить путь',
                    'remove_location': 'Удалить путь',
                    'apply_settings': 'Применить настройки',

                    # Errors
                    'error': 'Ошибка',
                    'file_not_found': 'Файл больше не существует:\n{}',
                    'invalid_regex': 'Некорректный regex-шаблон: {}',
                    'invalid_size': 'Некорректный формат размера: {}',
                    'invalid_date': 'Некорректный формат даты: {}',
                    'scan_failed': 'Сканирование завершилось ошибкой:\n{}',
                    'no_indices': 'Индексы поиска не найдены.',
                    'no_selection': 'Файлы не выбраны.',
                    'duplicate_folder': 'Эта папка уже в списке.',
                }
            }
        
        
        # Auto-detect system language with improved method
        self.current_lang = self._detect_system_language()
    
    def set_language(self, lang_code: str):
        """Set the current language."""
        if lang_code in self.translations:
            self.current_lang = lang_code
    
    def get(self, key: str, *args) -> str:
        """Get translated string, with optional formatting."""
        text = self.translations[self.current_lang].get(key, key)
        if args:
            try:
                return text.format(*args)
            except:
                return text
        return text

# Global translator instance
translator = Translator()