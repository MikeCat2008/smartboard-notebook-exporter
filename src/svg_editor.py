from lxml import etree

class SVGManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None
        self.main_group = None

    def load(self):
        # Load and validate SVG file
        funcion_tag = f"{__name__}.{self.__class__.__name__}.{self.load.__name__}"

        try:
            self.tree = etree.parse(self.file_path)

            # Search for "svg" tag at root level
            self.root = self.tree.getroot()
            if not self.root.tag.endswith("svg"):
                raise ValueError(f"{funcion_tag}: File '{self.file_path}' is not SVG.")

            # Search for "g" tag in first level of depth of root tag
            self.main_group = self.root.xpath("./g")
            if self.main_group == []:
                raise ValueError(f"{funcion_tag}: File '{self.file_path}' lacks required SVG tags.")

        except Exception as e:
            raise type(e)(f"{funcion_tag}: An error occurred while parsing '{self.file_path}': {e}")


    def get_svg_attributes(self, attr):
        # Search for 'attr' attribute inside <svg> root tag and return it as a list of strings.
        funcion_tag = f"{__name__}.{self.__class__.__name__}.{self.get_svg_attributes.__name__}"

        attr_str = self.root.get(str(attr))
        if attr_str:
            # Asumiendo que vienen como "x1 y1 x2 y2" o "x1,y1,x2,y2"
            # Reemplazamos comas por espacios y dividimos
            attr_clean_str = attr_str.replace(",", " ")
            attr_array = attr_clean_str.split()
            return attr_array

        print(f"{funcion_tag}: '{attr}' does not exist as an attribute inside '<svg>' root tag. Returning empty list.")
        return [] # Return empty list if attr_str is empty

    def update_svg_attributes(self, attrs_dict):
        # Update "<svg>" root tag using a dictionary

        for key, value in attrs_dict.items():
            self.root.set(key, str(value))

    def apply_main_group_transform(self, transform_str):
        if self.main_group != []:
            for group in self.main_group:
                group.set("transform", transform_str)

    def save(self, output_path):
        # Save file in binary mode
        with open(output_path, "wb") as f:
            f.write(etree.tostring(self.tree, encoding="utf-8", xml_declaration=True, pretty_print=True))

def main():
    print(f"\nsvg_editor: DEBUGGING: Called 'main()' funcion. Funcion is entended to be used for debugging.")

    print(f"\nsvg_editor: DEBUGGING: Testing class method 'SVGManager.load()'.")
    try:
        infile = input("SVG file full path: ")
        editor = SVGManager(infile)
        editor.load()
    except Exception as e:
        print(f"svg_editor: DEBUGGING: An error ocurred with 'SVGManager.load()': {e}")
        return

    print(f"\nsvg_editor: DEBUGGING: Testing class method 'SVGManager.get_svg_attributes()'.")
    try:
        print(f"'width': {editor.get_svg_attributes("width")}")
        print(f"'height': {editor.get_svg_attributes("height")}")
        print(f"'canvas_bounds': {editor.get_svg_attributes("canvas_bounds")}")
    except Exception as e:
        print(f"svg_editor: DEBUGGING: An error ocurred with 'SVGManager.get_svg_attributes()': {e}")
        return

    print(f"\nsvg_editor: DEBUGGING: Testing class method 'SVGManager.update_svg_attributes()'.")
    try:
        inattrs = input("Attributes (key=value, separated by comma ','): ")
        attrs = dict(item.split("=") for item in inattrs.replace(" ", "").split(","))
        editor.update_svg_attributes(attrs)
    except Exception as e:
        print(f"svg_editor: DEBUGGING: An error ocurred with 'SVGManager.update_svg_attributes()': {e}")
        return

    print(f"\nsvg_editor: DEBUGGING: Testing class method 'SVGManager.apply_main_group_transform()'.")
    try:
        # translate(X.xx,Y.yy)
        editor.apply_main_group_transform(input("Transform string: "))
    except Exception as e:
        print(f"svg_editor: DEBUGGING: An error ocurred with 'SVGManager.apply_main_group_transform()': {e}")

    print(f"\nsvg_editor: DEBUGGING: Testing class method 'SVGManager.save()'.")
    try:
        outfile = input("Full path for edited SVG file: ")
        editor.save(outfile)
    except Exception as e:
        print(f"svg_editor: DEBUGGING: An error ocurred with 'SVGManager.save()': {e}")
        return

    print(f"\nsvg_editor: DEBUGGING: No tests remaining. Bye! :3")

if __name__ == "__main__":
    print("svg_editor: 'svg_editor' is running as '__main__'. Program is entended to be used as a module.")
    main()
