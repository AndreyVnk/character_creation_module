from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    """Base character class."""
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'

    def __init__(self, name: str):
        self.name = name

    def attack(self) -> str:
        """Attack function."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный 'f'{value_attack}'

    def defence(self) -> str:
        """Defence function."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} урона'

    def special(self) -> str:
        """Special skill fucntion."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Warrior class."""
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_SKILL: str = 'Выносливость'
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS: str = ('дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')


class Mage(Character):
    """Mage class."""
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_SKILL: str = 'Атака'
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS: str = ('находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')


class Healer(Character):
    """Healer class."""
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_SKILL: str = 'Защита'
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS: str = ('могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """

    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input(
            'Введи название персонажа, '
            'за которого хочешь играть: Воитель — warrior, '
            'Маг — mage, Лекарь — healer: '
        )
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: Character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """

    class_trainings: dict = {
        'Warrior': 'ты Воитель — великий мастер ближнего боя.',
        'Mage': 'ты Маг — превосходный укротитель стихий.',
        'Healer': 'ты Лекарь — чародей, способный исцелять раны.'
    }
    print(f'{character.name}, {class_trainings[character.__class__.__name__]}')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    class_commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in class_commands:
            print(class_commands[cmd]())
    return 'Тренировка окончена.'


if __name__ == '__main__':
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    print(start_training(char_class))
