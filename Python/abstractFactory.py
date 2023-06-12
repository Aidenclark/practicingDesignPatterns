# Abstract Factory Interface
class UIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

# Concrete Factory for Windows UI
class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Concrete Factory for macOS UI
class MacOSUIFactory(UIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Abstract Product: Button
class Button:
    def render(self):
        pass

# Concrete Product: Windows Button
class WindowsButton(Button):
    def render(self):
        print("Rendering a Windows button.")

# Concrete Product: macOS Button
class MacOSButton(Button):
    def render(self):
        print("Rendering a macOS button.")

# Abstract Product: Checkbox
class Checkbox:
    def render(self):
        pass

# Concrete Product: Windows Checkbox
class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering a Windows checkbox.")

# Concrete Product: macOS Checkbox
class MacOSCheckbox(Checkbox):
    def render(self):
        print("Rendering a macOS checkbox.")

# Client code
def main():
    # Creating Windows UI
    windows_factory = WindowsUIFactory()
    windows_button = windows_factory.create_button()
    windows_checkbox = windows_factory.create_checkbox()

    windows_button.render()     # Output: Rendering a Windows button.
    windows_checkbox.render()   # Output: Rendering a Windows checkbox.

    # Creating macOS UI
    macos_factory = MacOSUIFactory()
    macos_button = macos_factory.create_button()
    macos_checkbox = macos_factory.create_checkbox()

    macos_button.render()       # Output: Rendering a macOS button.
    macos_checkbox.render()     # Output: Rendering a macOS checkbox.

if __name__ == '__main__':
    main()
